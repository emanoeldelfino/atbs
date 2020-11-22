#! python3
# mclip.py - A multi-clipboard program.

import sys
import pyperclip

text = {'agree': 'Yes, I agree. That sounds fine to me.',
        'busy': 'Sorry, can we do this later this week or next week? ',
        'upsell': 'Would you consider making this a monthly donation? '}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1].lower()  # first command line arg is the keyphrase

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There\'s no text for {keyphrase}.')

# mclip.bat on C:\Windows

# :: C:\Windows folder
# REM comment

# @py.exe "D:\Users\Emanoel Delfino\Desktop\Python\Automate The Boring Stuff\chapter 6\mclip.py" %*
# @pause  & :: Inline comment

# To run the code -> Win+R, inside text box put <mclip> <key phrase>
