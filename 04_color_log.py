import logging
from customlogformatter import CustomLogFormatter

# create logger with 'appname'
logger = logging.getLogger(__name__)

def logger_config():
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    handler.setFormatter(CustomLogFormatter())

    logger.addHandler(handler)


def main():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

if __name__ == "__main__":
    logger_config()
    main()