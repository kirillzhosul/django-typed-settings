import pytest

from django_typed_settings import (
    DjangoSettingsInvalidLoggingLevelError,
    DjangoSettingsMissingRequiredKeyError,
    env_key_logging_level,
)
from tests.conftest import set_environ_key


def test_env_key_logging_level_missing():
    with pytest.raises(DjangoSettingsMissingRequiredKeyError):
        assert env_key_logging_level("missing_key") is None
    assert env_key_logging_level("missing_key", default="FATAL") == "FATAL"


def test_env_key_logging_level_valid():
    set_environ_key("key", "FATAL")
    assert env_key_logging_level("key") == "FATAL"


def test_env_key_logging_level_value_error():
    set_environ_key("key", "invalid_level")
    with pytest.raises(DjangoSettingsInvalidLoggingLevelError):
        assert env_key_logging_level("key")
