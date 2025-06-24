from django_typed_settings.logging.configuration import django_logging_configuration


def test_django_logging_configuration():
    assert django_logging_configuration(
        disable_existing_loggers=False,
        filters={
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
        },
        formatters={
            "verbose": {
                "format": "[{levelname}]-[{asctime}]-[{module}]-[{process:d}]-[{thread:d}]: {message}",
                "style": "{",
            },
            "default": {
                "format": "[{levelname}]-[{asctime}]-[{module}]: {message}",
                "style": "{",
            },
            "simple": {"format": "[{levelname}]: {message}", "style": "{"},
        },
        handlers={
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "default",
                "filters": ["require_debug_true"],
            },
            "file": {
                "level": "DEBUG",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "django.log",
                "maxBytes": (1024**2) * 50,  # 50MB
                "backupCount": 5,
                "formatter": "default",
            },
        },
        loggers={
            "": {"handlers": ["file", "console"], "level": "DEBUG", "propagate": True},
            "daphne": {
                "handlers": ["file", "console"],
                "level": "DEBUG",
                "propagate": False,
            },
            "faker": {"handlers": ["file", "console"], "level": "ERROR"},
        },
    )
