import * as markdownlint from 'markdownlint';

const text1 = '| Component | Initial state | Root cause | Fix | Final verification |\n| --- | --- | --- | --- | --- |\n| Doctor |  |  |  |  |\n';
const text2 = '| #     Project |\n| ----  ------ |\n| 1     Banking |\n';
const text3 = '| #  | Project |\n|----|---------|\n| 1  | Banking |\n';
const text4 = '| #     Project                         Type |\n| ----  ------------------------------  ------ |\n| 1     Banking                         Fintech |\n';

const results = markdownlint.sync({strings: {t1: text1, t2: text2, t3: text3, t4: text4}, config: {'MD060': true}});
console.log('t1 (compact single-space):', JSON.stringify(results.t1));
console.log('t2 (padded):', JSON.stringify(results.t2));
console.log('t3 (compact):', JSON.stringify(results.t3));
console.log('t4 (aligned):', JSON.stringify(results.t4));
