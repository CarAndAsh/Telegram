from logging import getLogger, DEBUG, Formatter, StreamHandler, FileHandler
from sys import stdout

format = '[{asctime}]\t{levelname}\t{name}:{lineno}\t{filename}\n{message}'
formatter = Formatter(fmt=format, style='{')

stream = StreamHandler(stdout)
stream.setFormatter(formatter)
to_file = FileHandler('log.txt', 'w', encoding='utf-8')
to_file.setFormatter(formatter)

logger = getLogger()
logger.level = DEBUG
logger.addHandler(stream)
logger.addHandler(to_file)
