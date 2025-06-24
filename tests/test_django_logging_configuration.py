from django_typed_settings.logging.configuration import django_logging_configuration
from django_typed_settings.logging.spec import DJANGO_DEFAULT_LOGGING


def test_not_overrides_django_defaults():
    """Using `mutate_from_django_defaults` should not obscure defaults"""
    config = django_logging_configuration(
        mutate_from_django_defaults=True,
        handlers={},
        loggers={},
        filters={},
        formatters={},
    )

    assert config["filters"]
    assert config["formatters"]
    assert config["handlers"]
    assert config["loggers"]


def test_append_to_blank():
    """Rewriting without `mutate_from_django_defaults` should rewrite from scratch."""
    config = django_logging_configuration(
        mutate_from_django_defaults=False,
        handlers={"handler": {"level": "CRITICAL"}},
        loggers={"logger": {"level": "CRITICAL"}},
        filters={"filter": {"()": "filter"}},
        formatters={"formatter": {"validate": True}},
    )

    assert len(config["loggers"]) == 1
    assert len(config["filters"]) == 1
    assert len(config["handlers"]) == 1
    assert len(config["formatters"]) == 1
    assert config["version"] == 1


def test_mutates_properly():
    """Using `mutate_from_django_defaults` should append to existing defaults."""
    config = django_logging_configuration(
        mutate_from_django_defaults=True,
        handlers={"handler": {"level": "CRITICAL"}},
        loggers={"logger": {"level": "CRITICAL"}},
        filters={"filter": {"()": "filter"}},
        formatters={"formatter": {"validate": True}},
    )

    assert len(config["loggers"]) == len(DJANGO_DEFAULT_LOGGING["loggers"]) + 1
    assert len(config["filters"]) == len(DJANGO_DEFAULT_LOGGING["filters"]) + 1
    assert len(config["handlers"]) == len(DJANGO_DEFAULT_LOGGING["handlers"]) + 1
    assert len(config["formatters"]) == len(DJANGO_DEFAULT_LOGGING["formatters"]) + 1
