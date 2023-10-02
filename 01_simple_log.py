# reference : https://machinelearningmastery.com/logging-in-python/
import logging


def main():
	logging.debug('Debug message')
	logging.info('Info message')
	logging.warning('Warning message')
	logging.error('Error message')
	logging.critical('Critical message')


if __name__ == '__main__':
	main()
