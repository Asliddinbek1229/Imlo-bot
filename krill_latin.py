from transliterate import to_latin, to_cyrillic
def krill_latin(word):
    if word.isascii():
        response = to_cyrillic(word)
    else:
        response = to_latin(word)

    return response