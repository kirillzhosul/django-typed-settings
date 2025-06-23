from decimal import Decimal

import pytest

from django_typed_settings import env_key
from django_typed_settings.exceptions import (
    DjangoSettingsInvalidFlagValueError,
    DjangoSettingsKeyValueError,
)
from tests.conftest import set_environ_key


def test_env_key_missing():
    assert env_key("missing_key") is None
    assert env_key("missing_key", default=1) == 1


def test_env_key_valid():
    set_environ_key("key", "my_value")
    assert env_key("key", as_type=str) == "my_value"

    set_environ_key("key", "1")
    assert env_key("key", as_type=int) == 1

    set_environ_key("key", "2")
    value = env_key("key", as_type=float)
    assert isinstance(value, float)
    assert value == 2

    set_environ_key("key", "3")
    value = env_key("key", as_type=Decimal)
    assert isinstance(value, Decimal)
    assert value == 3


def test_env_key_value_error():
    set_environ_key("key", "value_error")
    with pytest.raises(DjangoSettingsKeyValueError):
        assert env_key("key", as_type=int) == "my_value"
    with pytest.raises(DjangoSettingsInvalidFlagValueError):
        assert env_key("key", as_type=bool) == "my_value"
    with pytest.raises(DjangoSettingsKeyValueError):
        assert env_key("key", as_type=float) == "my_value"
    with pytest.raises(DjangoSettingsKeyValueError):
        assert env_key("key", as_type=Decimal) == "my_value"
