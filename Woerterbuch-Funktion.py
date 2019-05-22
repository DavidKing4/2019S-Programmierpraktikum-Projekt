def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


import os

# working directory
os.getcwd()


# Um "working directory" zu ändern -->
os.chdir("")

