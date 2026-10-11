import { mkdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

// Invented teaching data, deliberately unrelated to SLN360 participant records.
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dataDir = path.join(root, 'data/synthetic');
const tflDir = path.join(root, 'tfl');
mkdirSync(dataDir, { recursive: true });
mkdirSync(tflDir, { recursive: true });
const study = 'EDU-LPA-001';
const visits = [{ day: 1, name: 'BASELINE' }, { day: 15, name: 'DAY 15' }, { day: 30, name: 'DAY 30' }, { day: 90, name: 'DAY 90' }];
const dateFor = day => new Date(Date.UTC(2026, 0, day)).toISOString().slice(0, 10);
const round = value => Number(value.toFixed(1));
const mean = values => values.reduce((sum, value) => sum + value, 0) / values.length;
const sd = values => Math.sqrt(values.reduce((sum, value) => sum + (value - mean(values)) ** 2, 0) / (values.length - 1));
const median = values => { const sorted = [...values].sort((a, b) => a - b); const middle = Math.floor(sorted.length / 2); return sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2; };
function csv(name, rows, directory = dataDir) {
  const columns = Object.keys(rows[0]);
  const escape = value => { const text = String(value ?? ''); return /[",\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text; };
  writeFileSync(path.join(directory, name), [columns.join(','), ...rows.map(row => columns.map(column => escape(row[column])).join(','))].join('\n') + '\n');
}
const dm = Array.from({ length: 24 }, (_, index) => {
  const i = index + 1;
  return { STUDYID: study, DOMAIN: 'DM', USUBJID: `EDU-LPA-${String(i).padStart(3, '0')}`, SUBJID: String(i).padStart(3, '0'), AGE: 36 + (i * 3) % 35, AGEU: 'YEARS', SEX: i % 3 === 0 ? 'F' : 'M', ARM: i % 2 ? 'Investigational A' : 'Placebo', RFSTDTC: dateFor(1), RFENDTC: dateFor(90) };
});
const ex = dm.map(subject => ({ STUDYID: study, DOMAIN: 'EX', USUBJID: subject.USUBJID, EXSEQ: 1, EXTRT: subject.ARM, EXDOSE: 1, EXDOSU: 'mL', EXSTDTC: dateFor(1) }));
const lb = [];
const vs = [];
const adsl = [];
const adlb = [];
dm.forEach((subject, index) => {
  const i = index + 1;
  const baseline = 150 + (i * 17) % 160;
  adsl.push({ STUDYID: study, USUBJID: subject.USUBJID, AGE: subject.AGE, SEX: subject.SEX, TRT01A: subject.ARM, SAFFL: 'Y', LPA_BASE: baseline });
  visits.forEach((visit, visitIndex) => {
    const missing = i === 7 && visit.day === 30;
    const fraction = subject.ARM === 'Investigational A' ? [1, 0.65, 0.4, 0.55][visitIndex] : [1, 1.02, 0.99, 1.01][visitIndex];
    const value = missing ? '' : round(baseline * fraction + (visitIndex === 0 ? 0 : (i % 5 - 2) * 2));
    lb.push({ STUDYID: study, DOMAIN: 'LB', USUBJID: subject.USUBJID, LBSEQ: visitIndex + 1, LBTESTCD: 'LPA', LBTEST: 'Lipoprotein(a)', LBORRES: value, LBORRESU: 'nmol/L', LBSTRESN: value, LBSTRESU: 'nmol/L', VISIT: visit.name, LBDY: visit.day, LBDTC: dateFor(visit.day), LBSTAT: missing ? 'NOT DONE' : '', LBREASND: missing ? 'SPECIMEN NOT AVAILABLE' : '' });
    adlb.push({ STUDYID: study, USUBJID: subject.USUBJID, TRT01A: subject.ARM, PARAMCD: 'LPA', AVISIT: visit.name, ADY: visit.day, AVAL: value, BASE: baseline, CHG: missing ? '' : round(value - baseline), PCHG: missing ? '' : round(100 * (value - baseline) / baseline), OBSFL: missing ? 'N' : 'Y' });
    for (const [test, label, unit, measure] of [['SYSBP', 'Systolic Blood Pressure', 'mmHg', 112 + (i * 7) % 25 + visitIndex], ['PULSE', 'Pulse Rate', 'beats/min', 60 + (i * 3) % 21 + visitIndex]]) {
      vs.push({ STUDYID: study, DOMAIN: 'VS', USUBJID: subject.USUBJID, VSSEQ: visitIndex * 2 + (test === 'SYSBP' ? 1 : 2), VSTESTCD: test, VSTEST: label, VSORRES: measure, VSORRESU: unit, VISIT: visit.name, VSDY: visit.day, VSDTC: dateFor(visit.day) });
    }
  });
});
const eventSpecs = [[3, 'Headache', 4], [3, 'Headache', 12], [5, 'Injection site discomfort', 2], [9, 'Nausea', 5], [11, 'Injection site discomfort', 3], [2, 'Headache', 6], [6, 'Rash', 8]];
const eventCounts = new Map();
const ae = eventSpecs.map(([id, term, day]) => {
  const subject = dm[id - 1];
  const seq = (eventCounts.get(id) ?? 0) + 1;
  eventCounts.set(id, seq);
  return { STUDYID: study, DOMAIN: 'AE', USUBJID: subject.USUBJID, AESEQ: seq, AETERM: term, AESEV: 'MILD', AESER: 'N', AESTDTC: dateFor(day), AEENDTC: dateFor(day + 1), AESTDY: day };
});
for (const [name, rows] of [['dm.csv', dm], ['ex.csv', ex], ['ae.csv', ae], ['vs.csv', vs], ['lb.csv', lb], ['adsl-teaching.csv', adsl], ['adlb-teaching.csv', adlb]]) csv(name, rows);

const arms = ['Placebo', 'Investigational A'];
const baselineRows = arms.map(arm => {
  const subjects = adsl.filter(row => row.TRT01A === arm);
  return { ARM: arm, N: subjects.length, AGE_MEAN: round(mean(subjects.map(row => row.AGE))), AGE_SD: round(sd(subjects.map(row => row.AGE))), FEMALE_N: subjects.filter(row => row.SEX === 'F').length, LPA_BASE_MEDIAN: median(subjects.map(row => row.LPA_BASE)) };
});
csv('baseline-summary.csv', baselineRows, tflDir);
const safetyRows = arms.flatMap(arm => {
  const subjects = dm.filter(row => row.ARM === arm);
  const ids = new Set(subjects.map(row => row.USUBJID));
  const events = ae.filter(row => ids.has(row.USUBJID));
  return ['Any recorded event', 'Headache', 'Injection site discomfort', 'Nausea', 'Rash'].map(term => {
    const selected = term === 'Any recorded event' ? events : events.filter(row => row.AETERM === term);
    const n = new Set(selected.map(row => row.USUBJID)).size;
    return { ARM: arm, TERM: term, DENOMINATOR: subjects.length, PARTICIPANTS_N: n, PARTICIPANTS_PCT: round(100 * n / subjects.length), EVENT_RECORDS_N: selected.length };
  });
});
csv('safety-summary.csv', safetyRows, tflDir);
const figureRows = arms.flatMap(arm => visits.map(visit => {
  const rows = adlb.filter(row => row.TRT01A === arm && row.ADY === visit.day && row.OBSFL === 'Y');
  return { ARM: arm, DAY: visit.day, VISIT: visit.name, N_OBSERVED: rows.length, MEAN_LPA: round(mean(rows.map(row => row.AVAL))) };
}));
csv('lpa-figure-data.csv', figureRows, tflDir);
const listing = adlb.filter(row => ['EDU-LPA-003', 'EDU-LPA-007'].includes(row.USUBJID)).map(row => ({ USUBJID: row.USUBJID, ARM: row.TRT01A, VISIT: row.AVISIT, LPA_NMOL_L: row.AVAL, STATUS: row.OBSFL === 'Y' ? 'Observed' : 'Not done: specimen not available' }));
csv('patient-listing.csv', listing, tflDir);
const title = '# Generated TFL examples — EDU-LPA-001\n\n**Invented teaching data. Not SLN360 results.** All 24 participants received their assigned invented intervention; each arm has 12.\n\n';
const table = (headers, rows) => `| ${headers.join(' | ')} |\n| ${headers.map(() => '---').join(' | ')} |\n${rows.map(row => `| ${row.join(' | ')} |`).join('\n')}\n\n`;
let report = title + '## Table 1 — Participant characteristics\n\n';
report += table(['Arm', 'N', 'Age mean (SD), years', 'Female n (%)', 'Baseline Lp(a) median, nmol/L'], baselineRows.map(row => [row.ARM, row.N, `${row.AGE_MEAN.toFixed(1)} (${row.AGE_SD.toFixed(1)})`, `${row.FEMALE_N} (${round(100 * row.FEMALE_N / row.N).toFixed(1)}%)`, row.LPA_BASE_MEDIAN]));
report += 'Descriptive summaries; the table is not a balance test. SD uses the sample definition. Baseline is observed for everyone.\n\n## Table 2 — Recorded adverse events\n\n';
report += table(['Arm', 'Event term', 'Participants n (%)', 'Event records'], safetyRows.map(row => [row.ARM, row.TERM, `${row.PARTICIPANTS_N}/${row.DENOMINATOR} (${row.PARTICIPANTS_PCT.toFixed(1)}%)`, row.EVENT_RECORDS_N]));
report += 'Counts refer to participants with at least one recorded event; repeated events count once per participant per term. The event-record column counts all records. All events are after dosing and mild; none are serious in this invented dataset. These are plain-language terms, not MedDRA-coded preferred terms. No safety-equivalence or causal conclusion is intended.\n\n## Figure 1 — Observed Lp(a) over time\n\n';
report += '![Observed mean Lp(a) in the invented study](lpa-over-time.svg)\n\n';
report += table(['Arm', 'Visit', 'Observed n', 'Mean Lp(a), nmol/L'], figureRows.map(row => [row.ARM, row.VISIT, row.N_OBSERVED, row.MEAN_LPA.toFixed(1)]));
report += 'Observed-case descriptive means: no imputation, confidence intervals, or treatment-effect estimation. Day 30 has one missing active-arm result. Do not read a changing observed-case mean as an unbiased causal estimate.\n\n## Listing 1 — Example participant laboratory records\n\n';
report += table(['Participant', 'Arm', 'Visit', 'Lp(a), nmol/L', 'Status'], listing.map(row => [row.USUBJID, row.ARM, row.VISIT, row.LPA_NMOL_L === '' ? '—' : row.LPA_NMOL_L.toFixed(1), row.STATUS]));
report += 'Selected participants only, not the whole study. A dash means no observed value, not zero.\n';
writeFileSync(path.join(tflDir, 'examples.md'), report);
console.log('Generated 24 participants, 7 AE records, 192 VS records, 96 LB records (95 observed), and descriptive TFLs.');
