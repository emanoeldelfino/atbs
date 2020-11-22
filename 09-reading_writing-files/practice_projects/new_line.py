def set_new_lines(string, max_chr=50):
    string = string.replace('\n', ' ')
    words = string.split()
    length = 0
    new = ''
    for word in words:
        length += len(word) + 1
        new += f'{word} ' if length < max_chr else f'{word}\n'
        if length >= max_chr:
            length = 0

    return new
