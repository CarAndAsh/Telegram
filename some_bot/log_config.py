from logging import getLogger, DEBUG, Formatter, StreamHandler, FileHandler
from sys import stdout

format = '[{asctime}]\t{levelname}\t{name}:{lineno}\t{filename}\t{message}'
formatter = Formatter(fmt=format, style='{')

stream = StreamHandler(stdout)
stream.setFormatter(formatter)
to_file = FileHandler('log.txt', 'w')
to_file.setFormatter(formatter)

logger = getLogger()
logger.level = DEBUG
logger.addHandler(stream)
logger.addHandler(to_file)
