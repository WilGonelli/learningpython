import random
from words_list import words

def random_word(category: str):
    return random.choice(words[category])

def verify_word(letters_correct: list[str], word: str):
    return "".join(letter if letter in letters_correct else "_" for letter in word )