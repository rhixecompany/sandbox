# Django Celery Reference

## Common Setup
```python
# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# tasks.py
@app.task
def my_task(param):
    return process(param)
```

## Key Commands
```bash
celery -A your_app worker -l info
celery -A your_app beat -l info
celery -A your_app flower  # Monitoring UI
```
