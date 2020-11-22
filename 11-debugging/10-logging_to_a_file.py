import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=''
                    '%(asctime)s - %(levelname)s - %(message)s')

logging.debug('A debug message.')
logging.info('Information about the code.')
logging.warning('Warning for some problem.')
logging.error('Some error happened.')
logging.critical('CRITICAL ERROR!')
