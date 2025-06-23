from django_typed_settings.database import env_key_database
from tests.conftest import set_environ_key


def test_env_key_database():
    set_environ_key("DJANGO_DATABASE_ENGINE", "django.db.backends.postgresql")

    set_environ_key("DJANGO_DATABASE_PASSWORD", "PASSWORD")
    assert env_key_database(always_use_engine="django.db.backends.postgresql")
