import os
from logging import getLogger, DEBUG, Formatter, StreamHandler, FileHandler
from sys import stdout

from bot_core.config import settings, BASE_DIR

formatter = Formatter(fmt=settings.log.log_format)

stream = StreamHandler(stdout)
stream.setFormatter(formatter)

if 'logs' not in os.listdir(BASE_DIR):
    os.mkdir(BASE_DIR / 'logs')
to_file = FileHandler(BASE_DIR / 'logs' / '.log.txt', 'w')
to_file.setFormatter(formatter)

logger = getLogger()
logger.level = DEBUG
logger.addHandler(stream)
logger.addHandler(to_file)
