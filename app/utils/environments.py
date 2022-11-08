import os

SYSTEM_LOG_FILE_PATH = os.getenv("SYSTEM_LOG_FILE_PATH", "questiondb.log")
DATABASE_LOG_FILE_PATH = os.getenv("DATABASE_LOG_FILE_PATH", "db.log")
SYSTEM__LOGGER_NAME = os.getenv("SYSTEM__LOGGER_NAME", "default")
DATABASE_LOGGER_NAME = os.getenv("DATABASE_LOGGER_NAME", "database")
