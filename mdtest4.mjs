import { micromark } from 'micromark';
import { gfmTable, gfmTableHtml } from 'micromark-extension-gfm-table';

// TRUE aligned: internal pipes at consistent columns
const aligned = '| #     | Project                         | Type        |\n| ----- | ------------------------------- | ----------- |\n| 1     | Banking                         | Fintech     |\n| 2     | comicwise                       | Streaming   |\n';
const html = micromark(aligned, { extensions: [gfmTable()], htmlExtensions: [gfmTableHtml()] });
console.log('RENDERS AS TABLE:', html.includes('<table>'));
console.log(html.replace(/\n/g, ' ').slice(0, 400));
