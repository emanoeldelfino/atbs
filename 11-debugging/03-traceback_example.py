import traceback
import datetime

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'a')
    errorFile.write(str(datetime.datetime.now()) + '\n')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')
