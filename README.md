# Django Typed Settings

Type safe API for bare django configuration settings system.
Alternative to `django-environ` and somehow `pydantic`

## Simple example

```python
# /settings.py

# Default Django way
TIMEOUT = 80                             # Hardcoded
TIMEOUT = os.environ.get("TIMEOUT", 80). # Environment, non-type safe

# Django Typed Settings
TIMEOUT = env_key('TIMEOUT', as_type=int, default=80) # Runtime checkable, type safe
```

## Features
- *Simple* API to fetch environment configurations like `10 days` or `disabled` into timedelta/booleans
- Utilities to setup database/cache(WIP, not yet)/logging
- 0 (zero) additional requirements.
- Type safety so using `f('key', as_type=str, default=80) => str | int`

## API
- `django_logging_configuration`
- `env_key`
- `env_key_required`
- `env_key_flag`
- `env_key_sequence`
- `env_key_timedelta`
- `env_key_database`