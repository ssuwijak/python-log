# reference : https://machinelearningmastery.com/logging-in-python/

import logging


def log_config(write_to_file = False):
    # level -> minimum level to be logged
    # ex. level=logging.DEBUG = minimum log is DEBUG level
    #     level=logging.WARNING = minimum log is WARNING level

    if write_to_file:
        logging.basicConfig(filename='file.log',
                            level=logging.DEBUG,
                            format='%(asctime)s : %(levelname)-8s : %(name)s : %(message)s')
    else:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s : %(levelname)-8s : %(name)s : %(message)s')


def main():
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')
    logging.critical('Critical message')


if __name__ == '__main__':
    log_config(True)
    main()
