# Python Debugpy Reference

## Common Setup
```python
import debugpy

# Allow remote connections
debugpy.listen(('0.0.0.0', 5678))
print('Waiting for debugger...')
debugpy.wait_for_client()
```

## VS Code Integration
```json
{
    "version": "0.2.0",
    "configurations": [{
        "name": "Python: Remote Attach",
        "type": "debugpy",
        "request": "attach",
        "connect": {"host": "localhost", "port": 5678}
    }]
}
```

## Key Commands
```bash
python -m debugpy --listen 5678 --wait-for-client app.py
```
