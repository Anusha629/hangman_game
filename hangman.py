import random

def get_random_word(wordlist="/usr/share/dict/words"):
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]

    for word in words:
            if not word.isalpha(): 
                continue
            if not word.islower():
                continue
            if len(word) < 5: 
                continue
            good_words.append(word)

    secret_word = random.choice(good_words)
    return secret_word
    





