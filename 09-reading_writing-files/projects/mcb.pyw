#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw del/delete <keyword> - Delete a keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw del/delete - Delete all keywords.

import shelve
import pyperclip
import sys
import pyinputplus as pyip

# mcb_shelf = shelve.open('mcb')

# Instead using a variable we can just use shelve.open() as a context manager:
with shelve.open('mcb') as mcb_shelf:
    # print(sys.argv)
    # print(sys.argv[0])

    # Save clipboard content.
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() in ['del', 'delete'] and sys.argv[2] in mcb_shelf:
            confirm = pyip.inputYesNo(prompt='Are you sure you want to delete it? [y/s] ')
            if confirm == 'yes':
                del mcb_shelf[sys.argv[2]]
        else:
            print('Error, invalid argument.')
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            # shelf_keys = mcb_shelf.keys()
            # pyperclip.copy(str(list(shelf_keys)))
            if mcb_shelf:
                shelf_keys = '\n'.join(mcb_shelf)
                print(shelf_keys)
                pyperclip.copy(shelf_keys)
            else:
                print('The shelf file is empty. There are no keywords, you can add a new one with:')
                print('    ~$ python [path\\]mcb.pyw save <keyword>')
        elif sys.argv[1].lower() in ['del', 'delete']:
            confirm = pyip.inputYesNo(prompt='Are you sure you want to delete the ENTIRE shelf? [y/s] ')
            if confirm == 'yes':
                mcb_shelf.clear()
                print('All the data was deleted. The shelf is now empty.')
        elif sys.argv[1] in mcb_shelf.keys():  # in (mcb_shelf.keys() == mcb_shelf)
            shelf_content = mcb_shelf[sys.argv[1]]
            pyperclip.copy(shelf_content)
        else:
            print('Error, invalid argument.')

mcb_shelf.close()
