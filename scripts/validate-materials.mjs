import assert from 'node:assert/strict';
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = file => readFileSync(path.join(root, file), 'utf8');
function csv(file) {
  // Current generated CSVs contain no embedded commas/newlines; reject surprises.
  const lines = read(file).trimEnd().split('\n');
  assert(!lines.some(line => line.includes('"')), `Quoted CSV needs a full parser: ${file}`);
  const headers = lines.shift().split(',');
  return lines.map(line => {
    const fields = line.split(',');
    assert.equal(fields.length, headers.length, `Column count: ${file}`);
    return Object.fromEntries(headers.map((name, i) => [name, fields[i]]));
  });
}
const dm = csv('data/synthetic/dm.csv');
assert.equal(dm.length, 24);
const identifiers = new Set(dm.map(row => row.USUBJID));
assert.equal(identifiers.size, 24);
for (const arm of ['Placebo', 'Investigational A']) assert.equal(dm.filter(row => row.ARM === arm).length, 12);
const expectedRows = { ex: 24, ae: 7, vs: 192, lb: 96 };
for (const [domain, expected] of Object.entries(expectedRows)) {
  const rows = csv(`data/synthetic/${domain}.csv`);
  assert.equal(rows.length, expected);
  const sequence = `${domain.toUpperCase()}SEQ`;
  const keys = new Set();
  for (const row of rows) {
    assert(identifiers.has(row.USUBJID), `Unknown participant in ${domain}`);
    assert.equal(row.STUDYID, 'EDU-LPA-001');
    assert.equal(row.DOMAIN, domain.toUpperCase());
    const key = `${row.USUBJID}:${row[sequence]}`;
    assert(!keys.has(key), `Duplicate key in ${domain}`);
    keys.add(key);
  }
}
const lb = csv('data/synthetic/lb.csv');
const missing = lb.filter(row => row.LBSTAT === 'NOT DONE');
assert.equal(missing.length, 1);
assert.equal(missing[0].USUBJID, 'EDU-LPA-007');
assert.equal(missing[0].LBDY, '30');
assert.equal(missing[0].LBORRES, '');
assert.equal(missing[0].LBSTRESN, '');
assert.equal(missing[0].LBREASND, 'SPECIMEN NOT AVAILABLE');
assert.equal(lb.filter(row => row.LBSTRESN !== '').length, 95);
const analysis = csv('data/synthetic/adlb-teaching.csv');
assert.equal(analysis.length, 96);
for (const row of analysis) {
  const source = lb.find(record => record.USUBJID === row.USUBJID && record.LBDY === row.ADY);
  assert.equal(row.AVAL, source.LBSTRESN);
  if (source.LBSTAT === 'NOT DONE') {
    assert.equal(row.OBSFL, 'N');
    assert.equal(row.CHG, '');
    assert.equal(row.PCHG, '');
  } else {
    assert.equal(row.OBSFL, 'Y');
    assert(Number.isFinite(Number(row.AVAL)));
  }
}
const safety = csv('tfl/safety-summary.csv');
for (const [arm, people, records] of [['Placebo', 2, 2], ['Investigational A', 4, 5]]) {
  const total = safety.find(row => row.ARM === arm && row.TERM === 'Any recorded event');
  assert.equal(Number(total.DENOMINATOR), 12);
  assert.equal(Number(total.PARTICIPANTS_N), people);
  assert.equal(Number(total.EVENT_RECORDS_N), records);
  assert(Math.abs(Number(total.PARTICIPANTS_PCT) - 100 * people / 12) < 0.051);
}
const headache = safety.find(row => row.ARM === 'Investigational A' && row.TERM === 'Headache');
assert.equal(Number(headache.PARTICIPANTS_N), 1);
assert.equal(Number(headache.EVENT_RECORDS_N), 2);
const baseline = csv('tfl/baseline-summary.csv');
assert.equal(Number(baseline.find(row => row.ARM === 'Placebo').LPA_BASE_MEDIAN), 223);
assert.equal(Number(baseline.find(row => row.ARM === 'Investigational A').LPA_BASE_MEDIAN), 216);
const figure = csv('tfl/lpa-figure-data.csv');
assert.equal(figure.length, 8);
for (const row of figure) {
  const ids = new Set(dm.filter(subject => subject.ARM === row.ARM).map(subject => subject.USUBJID));
  const source = lb.filter(record => ids.has(record.USUBJID) && record.LBDY === row.DAY && record.LBSTRESN !== '');
  assert.equal(Number(row.N_OBSERVED), source.length);
  const sum = source.reduce((total, record) => total + Number(record.LBSTRESN), 0);
  assert(Math.abs(Number(row.MEAN_LPA) - sum / source.length) < 0.051);
}
assert.equal(Number(figure.find(row => row.ARM === 'Investigational A' && row.DAY === '30').N_OBSERVED), 11);
assert.equal(csv('tfl/patient-listing.csv').length, 8);
assert(read('tfl/lpa-over-time.svg').includes('Invented EDU-LPA-001'));

for (let session = 1; session <= 3; session++) {
  const text = read(`docs/teaching/session-${session}.md`);
  const slots = [...text.matchAll(/^\| (\d+)–(\d+) \|/gm)].map(match => [Number(match[1]), Number(match[2])]);
  assert(slots.length > 0);
  assert.equal(slots[0][0], 0);
  assert.equal(slots.at(-1)[1], 120);
  for (let i = 0; i < slots.length; i++) {
    assert(slots[i][1] > slots[i][0]);
    if (i) assert.equal(slots[i][0], slots[i - 1][1]);
  }
  const breaks = [...text.matchAll(/^\| (\d+)–(\d+) \| Break \|/gm)];
  assert.equal(breaks.length, 1);
  assert.equal(Number(breaks[0][2]) - Number(breaks[0][1]), 10);
}
function markdownFiles(directory) {
  return readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
    if (entry.name.startsWith('.')) return [];
    const file = path.join(directory, entry.name);
    return entry.isDirectory() ? markdownFiles(file) : entry.name.endsWith('.md') ? [file] : [];
  });
}
for (const file of markdownFiles(root)) {
  const text = readFileSync(file, 'utf8');
  for (const match of text.matchAll(/\]\(([^\s)]+)\)/g)) {
    const target = match[1];
    if (/^[a-z]+:/i.test(target)) continue;
    const [relative, fragment] = target.split('#');
    const resolved = relative ? path.resolve(path.dirname(file), decodeURIComponent(relative)) : file;
    assert(existsSync(resolved), `Broken link in ${path.relative(root, file)}: ${target}`);
    if (fragment && resolved.endsWith('.md')) {
      const headings = [...readFileSync(resolved, 'utf8').matchAll(/^#{1,6} (.+)$/gm)].map(heading => heading[1].toLowerCase().replace(/[^\p{L}\p{N}_ -]/gu, '').replaceAll(' ', '-'));
      assert(headings.includes(fragment), `Broken heading link: ${target}`);
    }
  }
}
console.log('Validated synthetic relationships, missingness, TFL counts/means, figure, three 120-minute schedules, and local links.');
