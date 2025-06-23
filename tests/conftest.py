from os import environ


def set_environ_key(key: str, value: str) -> None:
    if key in environ:
        del environ[key]
    environ.setdefault(key, value)
