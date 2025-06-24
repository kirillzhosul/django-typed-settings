from .spec import LOGGING_LEVELS


class DjangoSettingsInvalidLoggingLevelError(Exception):
    def __init__(
        self,
        key: str,
        value: str,
    ) -> None:
        super().__init__(
            f"Expected logging level in environment key `{key}` but got `{value}` expected it to be an logging level (Valid values: {', '.join(LOGGING_LEVELS)})!"
        )
