import string

contents = open("pg10.txt").read().split()
punctuation = """!"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"""


def is_letter(l):
    isletter = l.isalpha()
    return isletter


def test_word(word):
    contains_letters = word.islower()
    return contains_letters


def parse_contents(bible):
    words = {}
    for word in bible:
        if test_word(word.lower()):
            if word not in words:
                words[word.lower()] = 1
            else:
                words[word.lower()] += 1
    return words


print(parse_contents(contents))
