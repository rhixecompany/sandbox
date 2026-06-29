# Client Management Pattern

> Extracted from `dataverse-python-production-code.prompt.md`.

## Client Management Pattern

```python
class DataverseService:
    _instance = None
    _client = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, org_url, credential):
        if self._client is None:
            self._client = DataverseClient(org_url, credential)

    @property
    def client(self):
        return self._client
```
