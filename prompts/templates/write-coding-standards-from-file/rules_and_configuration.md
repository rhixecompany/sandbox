# Rules and Configuration

> Extracted from `write-coding-standards-from-file.prompt.md`.

## Rules and Configuration

Below is a set of quasi-configuration `boolean` and `string[]` variables. Conditions for handling `true`, or other values for each variable are under the level two heading `## Variable and Parameter Configuration Conditions`.

Parameters for the prompt have a text definition. There is one required parameter **`${fileName}`**, and several optional parameters **`${folderName}`**, **`${instructions}`**, and any **`[configVariableAsParameter]`**.

### Configuration Variables

- addStandardsTest = false;
- addToREADME = false;
- addToREADMEInsertions = ["atBegin", "middle", "beforeEnd", "bestFitUsingContext"];
  - Default to **beforeEnd**.
- createNewFile = true;
- fetchStyleURL = true;
- findInconsistencies = true;
- fixInconsistencies = true;
- newFileName = ["CONTRIBUTING.md", "STYLE.md", "CODE_OF_CONDUCT.md", "CODING_STANDARDS.md", "DEVELOPING.md", "CONTRIBUTION_GUIDE.md", "GUIDELINES.md", "PROJECT_STANDARDS.md", "BEST_PRACTICES.md", "HACKING.md"];
  - For each file in `${newFileName}`, if file does not exist, use that file name and `break`, else continue to next file name of `${newFileName}`.
- outputSpecToPrompt = false;
- useTemplate = "verbose"; // or "v"
  - Possible values are `[["v", "verbose"], ["m", "minimal"], ["b", "best fit"], ["custom"]]`.
  - Selects one of the two example templates at the bottom of prompt file under the level two heading `## Coding Standards Templates`, or use another composition that is a better fit.
  - If **custom**, then apply per request.

### Configuration Variables as Prompt Parameters

If any of the variable names are passed to prompt as-is, or as a similar but clearly related text value, then override the default variable value with the value passed to prompt.

### Prompt Parameters

- **fileName** = The name of the file that will be analyzed in terms of: indentation, variable naming, commenting, conditional procedures, functional procedures, and other syntax related data for the coding language of the file.
- folderName = The name of the folder that will be used to extract data from multiple files into one aggregated dataset that will be analyzed in terms of: indentation, variable naming, commenting, conditional procedures, functional procedures, and other syntax related data for the coding language of the files.
- instructions = Additional instructions, rules, and procedures that will be provided for unique cases.
- [configVariableAsParameter] = If passed will override the default state of the configuration variable. Example:
  - useTemplate = If passed will override the configuration `${useTemplate}` default. Values are `[["v", "verbose"], ["m", "minimal"], ["b", "best fit"]]`.

#### Required and Optional Parameters

- **fileName** - required
- folderName - _optional_
- instructions - _optional_
- [configVariableAsParameter] - _optional_
