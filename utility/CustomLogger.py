import inspect
import logging
from inspect import stack
from venv import logger

def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]

    logger=logging.getLogger(loggerName)
    logger.setLevel(logLevel)

    fileHandler=logging.FileHandler("automation.log",mode='a')
    fileHandler.setLevel(logLevel)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
