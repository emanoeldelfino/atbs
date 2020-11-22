from pathlib import Path
import sys


def isThereFlashDrive():
    o_s = sys.platform  # win32, darwin, linux
    if o_s == 'win32':
        path_object = Path('D:/')
    elif o_s == 'linux':
        path_object = Path('/dev/sdb1')

    return path_object.exists()


detect_fd = isThereFlashDrive()
print(detect_fd)

# os.path.exists(path) acts much like path_object.exists(), it accepts Path objects as well as strings of
# file paths.

# This is also true for os.path.isfile(path) and os.path.isdir(path).
# Which are like path_object.is_file() and path_object.is_dir()
