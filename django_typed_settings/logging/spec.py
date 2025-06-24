import sys
from typing import Any, Literal, Required, TypedDict

# https://docs.python.org/3/library/logging.html#logging.Formatter
STYLE_T = Literal["%", "{", "$"]

# Known levels for logging module.
type LOGGING_LEVEL_T = Literal[
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARN",
    "WARNING",
    "INFO",
    "DEBUG",
    "NOTSET",
]
LOGGING_LEVELS: tuple[LOGGING_LEVEL_T, ...] = (
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARN",
    "WARNING",
    "INFO",
    "DEBUG",
    "NOTSET",
)


class DjangoLoggingConfigurationSpec(TypedDict, total=True):
    """Resulting specification for Django `LOGGING` configuration

    https://docs.djangoproject.com/en/5.2/topics/logging/#configuring-logging
    """

    version: int
    disable_existing_loggers: bool
    filters: dict[str, dict[str, str]]
    formatters: dict[str, "DjangoLoggingFormatterSpec"]
    # Is there any way to not bypass typecheck?
    handlers: dict[str, "DjangoLoggingHandlerSpec | dict[str, Any]"]
    loggers: dict[str, "DjangoLoggingLoggerSpec"]


type FILTERS_T = dict[str, dict[str, str]] | None
type LOGGERS_T = dict[str, DjangoLoggingLoggerSpec] | None
type FORMATTERS_T = dict[str, DjangoLoggingFormatterSpec] | None
type HANDLERS_T = dict[str, DjangoLoggingHandlerSpec | dict[str, Any]] | None


# https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
DjangoLoggingHandlerSpec = TypedDict(
    "DjangoLoggingHandlerSpec",
    {
        "class": Required[str],
        "level": LOGGING_LEVEL_T,
        "filters": list[str],
        # We cannot specify that extra fields (kwargs) passed to handler is typed
        # as there is different custom handlers and only way is to union these types (`spec | dict[...]``)
    },
    total=False,
)

# https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
DjangoLoggingLoggerSpec = TypedDict(
    "DjangoLoggingLoggerSpec",
    {
        "handlers": list[str],
        "filters": list[str],
        "level": LOGGING_LEVEL_T,
        "propagate": bool,
    },
    total=False,
)

# https://docs.python.org/3/library/logging.html#logging.Formatter
if sys.version_info >= (3, 10):
    DjangoLoggingFormatterSpec = TypedDict(
        "DjangoLoggingFormatterSpec",
        {
            "format": str,
            "datefmt": str,
            "validate": bool,
            "defaults": dict[str, Any],
            "style": STYLE_T,
            "class": str,
            "()": str,
        },
        total=False,
    )
elif sys.version_info >= (3, 8):
    DjangoLoggingFormatterSpec = TypedDict(
        "DjangoLoggingFormatterSpec",
        {
            "format": str,
            "datefmt": str,
            "validate": bool,
            "style": STYLE_T,
            "class": str,
            "()": str,
        },
        total=False,
    )
elif sys.version_info >= (3, 2):
    DjangoLoggingFormatterSpec = TypedDict(
        "DjangoLoggingFormatterSpec",
        {
            "format": str,
            "datefmt": str,
            "style": STYLE_T,
            "class": str,
            "()": str,
        },
        total=False,
    )
else:
    DjangoLoggingFormatterSpec = TypedDict(
        "DjangoLoggingFormatterSpec",
        {
            "format": str,
            "datefmt": str,
            "class": str,
            "()": str,
        },
        total=False,
    )

# https://github.com/django/django/blob/main/django/utils/log.py
DJANGO_DEFAULT_LOGGING: DjangoLoggingConfigurationSpec = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
