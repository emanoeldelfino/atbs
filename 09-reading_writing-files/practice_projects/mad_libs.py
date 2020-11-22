import sys
import string
from new_line import set_new_lines

letters = string.ascii_letters

# Create text file if it doesn't exist.
try:
    file = open('file.txt')
    file.close()
except FileNotFoundError:
    with open('file.txt', 'w') as f:
        f.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was\n\
unaffected by these events.')

    print('-> file.txt created successfully, you can replace the words ADJECTIVE, NOUN, \
ADVERB and VERB with any words you want.')
    print('-> The file is created with a sample text by default, you can replace that with any other \
text that you want.')
    sys.exit()

# Read from text file replacing ADJECTIVE, NOUN, ADVERB and VERB with
# user given words for these.
replace_words = 'ADJECTIVE', 'ADVERB', 'NOUN', 'VERB'

new_content = ''

with open('file.txt') as f:
    content = f.read()
    file_words = content.split()
    for file_word in file_words:
        new_file_word = ''
        last_characters = ''
        if file_word[-1] not in letters:
            for character in file_word:
                if character in letters:
                    new_file_word += character
                else:
                    last_characters += character
        else:
            new_file_word = file_word

        if new_file_word in replace_words:
            replaced_word = input(f"Enter {'a' if new_file_word in ['NOUN', 'VERB'] else 'an'}\
 {new_file_word.lower()}: ")
            new_content += replaced_word + last_characters + ' '
        else:
            new_content += file_word + ' '

# Create new text file from that.
print(new_content)
new_content = set_new_lines(new_content, max_chr=70)
with open('new_file.txt', 'w') as f:
    f.write(new_content)
