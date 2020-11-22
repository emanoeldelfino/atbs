import pprint  # p = pretty print, so pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)  # The output looks much cleaner, with the keys sorted.

print(pprint.pformat(count))  # Same as above, but you can get the string of it.
