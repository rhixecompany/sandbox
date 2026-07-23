# Variable and Parameter Configuration Conditions

> Extracted from `write-coding-standards-from-file.prompt.md`.

## Variable and Parameter Configuration Conditions

### `${fileName}.length > 1 || ${folderName} != undefined`

- If true, toggle `${fixInconsistencies}` to false.

### `${addToREADME} == true`

- Insert the coding standards into the `README.md` instead of outputting to the prompt or creating a new file.
- If true, toggle both `${createNewFile}` and `${outputSpecToPrompt}` to false.

### `${addToREADMEInsertions} == "atBegin"`

- If `${addToREADME}` is true, then insert the coding standards data at the **beginning** of the `README.md` file after the title.

### `${addToREADMEInsertions} == "middle"`

- If `${addToREADME}` is true, then insert the coding standards data at the **middle** of the `README.md` file, changing the standards title heading to match that of the `README.md` composition.

### `${addToREADMEInsertions} == "beforeEnd"`

- If `${addToREADME}` is true, then insert the coding standards data at the **end** of the `README.md` file, inserting a new line after the last character, then inserting the data on a new line.

### `${addToREADMEInsertions} == "bestFitUsingContext"`

- If `${addToREADME}` is true, then insert the coding standards data at the **best fitting line** of the `README.md` file in regards to the context of the `README.md` composition and flow of data.

### `${addStandardsTest} == true`

- Once the coding standards file is complete, write a test file to ensure the file or files passed to it adhere to the coding standards.

### `${createNewFile} == true`

- Create a new file using the value, or one of the possible values, from `${newFileName}`.
- If true, toggle both `${outputSpecToPrompt}` and `${addToREADME}` to false.

### `${fetchStyleURL} == true`

- Additionally use the data fetched from the links nested under level three heading `### Fetch Links` as context for creating standards, specifications, and styling data for the new file, prompt, or `README.md`.
- For each relevant item in `### Fetch Links`, run `#fetch ${item}`.

### `${findInconsistencies} == true`

- Evaluate syntax related to indentations, line-breaks, comments, conditional and function nesting, quotation wrappers i.e. `'` or `"` for strings, etc., and categorize.
- For each category, make a count, and if one item does not match the majority of the count, then commit to temporary memory.
- Depending on the status of `${fixInconsistencies}`, either edit and fix the low count categories to match the majority, or output to prompt inconsistencies stored in temporary memory.

### `${fixInconsistencies} == true`

- Edit and fix the low count categories of syntax data to match the majority of corresponding syntax data using inconsistencies stored in temporary memory.

### `typeof ${newFileName} == "string"`

- If specifically defined as a `string`, create a new file using the value from `${newFileName}`.

### `typeof ${newFileName} != "string"`

- If **NOT** specifically defined as a `string`, but instead an `object` or an array, create a new file using a value from `${newFileName}` by applying this rule:
  - For each file name in `${newFileName}`, if file does not exist, use that file name and `break`, else continue to the next.

### `${outputSpecToPrompt} == true`

- Output the coding standards to the prompt instead of creating a file or adding to README.
- If true, toggle both `${createNewFile}` and `${addToREADME}` to false.

### `${useTemplate} == "v" || ${useTemplate} == "verbose"`

- Use data under the level three heading `### "v", "verbose"` as guiding template when composing the data for coding standards.

### `${useTemplate} == "m" || ${useTemplate} == "minimal"`

- Use data under the level three heading `### "m", "minimal"` as guiding template when composing the data for coding standards.

### `${useTemplate} == "b" || ${useTemplate} == "best"`

- Use either the data under the level three heading `### "v", "verbose"` or `### "m", "minimal"`, depending on the data extracted from `${fileName}`, and use the best fit as guiding template when composing the data for coding standards.

### `${useTemplate} == "custom" || ${useTemplate} == "<ANY_NAME>"`

- Use the custom prompt, instructions, template, or other data passed as guiding template when composing the data for coding standards.
