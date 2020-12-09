from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(__file__).resolve().parent.parent


# def get_console_handler():
#     console_handler = logging.StreamHandler(sys.stdout)
#     console_handler.setFormatter(FORMATTER)
#     return console_handler

# def get_file_handler():
#     file_handler = TimedRotatingFileHandler(
#         LOG_FILE, when='midnight')

#     file_handler.setFormatter(FORMATTER)

#     return file_handler

# def get_logger(*,logger_name):
#     """Get logger with prepared handlers."""

#     logger = logging.getLogger(logger_name)

#     logger.addHandler(get_console_handler())
#     logger.addHandler(get_file_handler())
#     logger.propagate = False

#     return logger


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'things-mean-to-be-changed'
    SERVER_PORT = 5000


class ProductionConfig(Config):
    DEBUG = False
    SERVER_PORT = os.environ.get('PORT',5000)

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestConfig(Config):
    TESTING = True