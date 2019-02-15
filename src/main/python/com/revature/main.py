#!/usr/bin/env python3

'''
This is your main script, this should call several other scripts within your packages.
'''

import logging
import logging.config
from controller import controller
import os
# from io.data_access import register
# import io.data_access as data_access
# import service.business_logic as business_logic
# from error import custom_error
# import yaml

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

def main():
	print('TO-DO')
    # os.sys()

def simple_logging():
	'''
    -> Use the same name of logger to get the same object back in another class
    -> Create it first in your main script
    -> You could also declare it just once in the global scope of your main script
    -> If no name is provided, you get the "root" logger
    '''
    # logger = logging.getLogger('8-logging')

	# logging.basicConfig(level=logging.DEBUG, filename='/var/log/my_script/basic.log')
	
	logger.debug('Use it for tracing')
	logger.info('Use it for informational messages')
	logger.warning('Use it for operations that may raise errors')
	logger.error('Use it to notify a raise')
	logger.critical('Use it to notify of a critical issue (exit the app usually)')
	# logger = logging.getLogger('main')

'''
-> specifying optional values for the yaml configuration location
and the level
'''
def configured_logging(config_path='../../../../resources/logging.yaml'):
    # if os.path.exists(config_path):
    #     with open(config_path,'r') as f:
    #         config = yaml.safe_load(f.read())
        
    #     #Enable our loaded configuration
    #     logging.config.dictConfig(config)
    # else:
    #     raise ValueError('Logging configuration not found')

    #Test our configuration
    logger = logging.getLogger('8-logging')

    #Goes to a file
    logger.info('I have configured logging through a file')

    #Goes to another file
    logger.error('I have configured logging through a file')

    #Goes to the console
    logger.debug('I have configured logging through a file')

if __name__ == '__main__':
	main()