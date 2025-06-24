"""Django logging configuration constructor."""

from .spec import (
    DJANGO_DEFAULT_LOGGING,
    FILTERS_T,
    FORMATTERS_T,
    HANDLERS_T,
    LOGGERS_T,
    DjangoLoggingConfigurationSpec,
)


def django_logging_configuration(
    *,
    mutate_from_django_defaults: bool = True,
    disable_existing_loggers: bool = False,
    version: int = 1,
    filters: FILTERS_T = None,
    loggers: LOGGERS_T = None,
    formatters: FORMATTERS_T = None,
    handlers: HANDLERS_T = None,
) -> DjangoLoggingConfigurationSpec:
    """Construct `LOGGING` settings dict type as specification.

    :param mutate_from_django_defaults: If true, will append your given config to default Django one.

    https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
    https://docs.djangoproject.com/en/5.2/topics/logging/#configuring-logging
    """
    config: DjangoLoggingConfigurationSpec = {
        "version": version,
        "disable_existing_loggers": disable_existing_loggers,
        "filters": filters or {},
        "formatters": formatters or {},
        "handlers": handlers or {},
        "loggers": loggers or {},
    }
    if mutate_from_django_defaults:
        return {
            "version": version,
            "disable_existing_loggers": disable_existing_loggers,
            "filters": {**DJANGO_DEFAULT_LOGGING["filters"], **config["filters"]},
            "formatters": {
                **DJANGO_DEFAULT_LOGGING["formatters"],
                **config["formatters"],
            },
            "handlers": {**DJANGO_DEFAULT_LOGGING["handlers"], **config["handlers"]},
            "loggers": {**DJANGO_DEFAULT_LOGGING["loggers"], **config["loggers"]},
        }
    return config
