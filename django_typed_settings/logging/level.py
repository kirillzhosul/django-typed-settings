from django_typed_settings.environ import env_key, env_key_required

from .exceptions import DjangoSettingsInvalidLoggingLevelError
from .spec import LOGGING_LEVEL_T, LOGGING_LEVELS


def env_key_logging_level(
    key: str,
    default: LOGGING_LEVEL_T | None = None,
) -> LOGGING_LEVEL_T:
    """
    Return logging level key from environment variable and optional default fallback (or raise error).
    No way to acquire None on missing key.

    :param key: Name of key to load from environment.
    :param default: Value to return when there is no such key or None if strict.

    :returns: Value from environment as valid logging level.

    :raises DjangoSettingsMissingRequiredKeyError: If key is missing and default is None
    """
    raw_level = (
        env_key_required(key, as_type=str)
        if default is None
        else env_key(key, as_type=str, default=default)
    )
    if raw_level not in LOGGING_LEVELS:
        if default:
            return default
        raise DjangoSettingsInvalidLoggingLevelError(key, raw_level)
    return raw_level
