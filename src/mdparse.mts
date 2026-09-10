import { micromark } from "micromark";
import { gfmTable, gfmTableHtml } from "micromark-extension-gfm-table";

const t5 = "| A     B |\n| ----  --- |\n| 1     x |\n";
const t6 = "| A | B |\n| --- | --- |\n| 1 | x |\n";
const t7 =
	"| #     Project                         Type |\n| ----  ------------------------------  ------ |\n| 1     Banking                         Fintech |\n";

for (const [name, t] of [
	["t5-spaces-only", t5],
	["t6-pipes", t6],
	["t7-repo-style", t7],
]) {
	const html = micromark(t, { extensions: [gfmTable()], htmlExtensions: [gfmTableHtml()] });
	console.log(name, "=>", html.replace(/\n/g, " ").slice(0, 220));
}
