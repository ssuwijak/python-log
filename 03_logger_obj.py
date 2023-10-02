import logging

"""
Logger: An object named a logger represents a named channel for message logging. 
        You can add several loggers to your program, each with a unique name and 
        set of configurations. The name of the logger you want to use is specified 
        when you log a message.

"""
logger = logging.getLogger(__name__)

def log_config():
    # Create a custom formatter with your desired time format
    time_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)8s - %(name)s - %(message)s', datefmt=time_format)

    # Create a logger and set the custom formatter
    # logger = logging.getLogger('ccc')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set the log level (optional, can be DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.DEBUG)


def main():
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')


if __name__ == '__main__':
    log_config()
    main()
