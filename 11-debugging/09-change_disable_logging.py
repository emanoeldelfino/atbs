import logging
# Get only INFO and higher levels. DEBUG is skipped.
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging information.')         # Skipped because of level

logging.critical('Critical error! Critical error!')  # Showed

# It disable current level and lower ones.
# As it is CRITICAL which is the highest level it disables all logging messages.
# You'll probably want to add it near the import logging line of code in your program.
# So it'll be easier to find it and comment out or uncomment to enable or disable it as
# needed.
logging.disable(logging.CRITICAL)

logging.critical('Critical error! Critical error!')  # Skipped because of logging.disable
logging.error('Error! Error!')                       # Same as above
