import logging.config

from utils.environments import (
    SYSTEM_LOG_FILE_PATH,
    DATABASE_LOG_FILE_PATH,
    SYSTEM__LOGGER_NAME,
    DATABASE_LOGGER_NAME,
)

CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "class": "logging.Formatter",
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "default",
            "filename": SYSTEM_LOG_FILE_PATH,
            "mode": "a",
        },
        "database": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "default",
            "filename": DATABASE_LOG_FILE_PATH,
            "mode": "a",
        },
    },
    "loggers": {
        SYSTEM__LOGGER_NAME: {"handlers": ["console", "file"], "level": "DEBUG"},
        DATABASE_LOGGER_NAME: {"handlers": ["database"], "level": "DEBUG"},
    },
}


logging.config.dictConfig(CONFIG)


class LocalLogging:
    def __init__(self, logger: str) -> None:
        self.logger = logging.getLogger(logger)

    def info(self, *args, **kwargs) -> None:
        self.logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs) -> None:
        self.logger.warning(*args, **kwargs)

    def critical(self, *args, **kwargs) -> None:
        self.logger.critical(*args, **kwargs)
