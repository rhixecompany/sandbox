import { micromark } from 'micromark';
import { gfmTable, gfmTableHtml } from 'micromark-extension-gfm-table';
const t = '| #     Project                         Type        |\n| ----  ------------------------------  ----------- |\n| 1     Banking                         Fintech     |\n';
const html = micromark(t, { extensions: [gfmTable()], htmlExtensions: [gfmTableHtml()] });
console.log(html.slice(0, 300));
