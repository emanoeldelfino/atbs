import pyperclip
import re

cpfRegex = re.compile(r'''(
    (
        (\d{3})   # 3 numbers of cpf, similar to the social secutiry number in US
        (\.|-)    # sep
    ) {3}
    (\d{2})       # last two digits
    )''', re.VERBOSE)

text = str(pyperclip.paste())

new = cpfRegex.sub('XXX.XXX.XXX-XX', text)

pyperclip.copy(new)
print('Copied to clipboard')
print(new)
