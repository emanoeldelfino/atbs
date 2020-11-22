#! python3
# clearPhrases.py - Remove repeated words, spaces in text and '!' or '?' at the end of phrases.

import pyperclip
import re


def repl(match):
    pass

text = str(pyperclip.paste())

wordsRegex = re.compile(r'((\b\S+\b)\s+\b(\2)\b)')
new_text = wordsRegex.sub(r'\2', text)

# spacesRegex = re.compile(r'(\W?\s{2,}\W?)')
# new = spacesRegex.sub(' ', text)

punctuationRegex = re.compile(r'(.(!|\?){2,})')
for groups in punctuationRegex.findall(new_text):
    words = new_text.split()
    new = []

    for word in words:
        if '!' in word:
            word = word.replace('!', '')
            word += '!'
        if '?' in word:
            word = word.replace('?', '')
            word += '?'

        new.append(word)

    new_text = ' '.join(new)

pyperclip.copy(new_text)
print('Copied to clipboard')
print(new_text)
