# Configuration Reference

> Extracted from `add-educational-comments.prompt.md`.

## Configuration Reference

### Properties

- **Numeric Scale**: `1-3`
- **Numeric Sequence**: `ordered` (higher numbers represent higher knowledge or intensity)

### Parameters

- **File Name** (required): Target file(s) for commenting.
- **Comment Detail** (`1-3`): Depth of each explanation (default `2`).
- **Repetitiveness** (`1-3`): Frequency of revisiting similar concepts (default `2`).
- **Educational Nature**: Domain focus (default `Computer Science`).
- **User Knowledge** (`1-3`): General CS/SE familiarity (default `2`).
- **Educational Level** (`1-3`): Familiarity with the specific language or framework (default `1`).
- **Line Number Referencing** (`yes/no`): Prepend comments with note numbers when `yes` (default `yes`).
- **Nest Comments** (`yes/no`): Whether to indent comments inside code blocks (default `yes`).
- **Fetch List**: Optional URLs for authoritative references.

If a configurable element is missing, use the default value. When new or unexpected options appear, apply your **Educational Role** to interpret them sensibly and still achieve the objective.

### Default Configuration

- File Name
- Comment Detail = 2
- Repetitiveness = 2
- Educational Nature = Computer Science
- User Knowledge = 2
- Educational Level = 1
- Line Number Referencing = yes
- Nest Comments = yes
- Fetch List:
  - <https://peps.python.org/pep-0263/>
