# Code Structure

> Extracted from `dataverse-python-production-code.prompt.md`.

## Code Structure

1. Imports (stdlib, then third-party, then local)
2. Constants and enums
3. Logging configuration
4. Helper functions
5. Main service classes
6. Error handling classes
7. Usage examples

# User Request Processing

When user asks to generate code, provide:

1. **Imports section** with all required modules
2. **Configuration section** with constants/enums
3. **Main implementation** with proper error handling
4. **Docstrings** explaining parameters and return values
5. **Type hints** for all functions
6. **Usage example** showing how to call the code
7. **Error scenarios** with exception handling
8. **Logging statements** for debugging

# Quality Standards

- ✅ All code must be syntactically correct Python 3.10+
- ✅ Must include try-except blocks for API calls
- ✅ Must use type hints for function parameters and return types
- ✅ Must include docstrings for all functions
- ✅ Must implement retry logic for transient failures
- ✅ Must use logger instead of print() for messages
- ✅ Must include configuration management (secrets, URLs)
- ✅ Must follow PEP 8 style guidelines
- ✅ Must include usage examples in comments
