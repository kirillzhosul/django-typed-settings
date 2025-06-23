from datetime import timedelta

from django_typed_settings import env_key_timedelta
from tests.conftest import set_environ_key


def test_env_key_timedelta_valid():
    set_environ_key("key", "15d")
    assert env_key_timedelta("key") == timedelta(days=15)
    set_environ_key("key", "32h")
    assert env_key_timedelta("key") == timedelta(hours=32)
