#! python3
# 6-logging_module.py

import logging

# specify what dtails about LogRecord object you want
# to see and how you want those details displayed.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -'
                    '%(levelname)s - %(message)s')
