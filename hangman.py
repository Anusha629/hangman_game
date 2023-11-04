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

def get_mask_word(word, guesses):
    masked_word = []
    for i in word:
        if i in guesses:
            masked_word.append(i)
        else:
            masked_word.append("-")
    return "".join(masked_word)

def get_status(secret_word, turns_remaining, guesses):
    masked_word = get_mask_word(secret_word, guesses)
    guesses = "".join(guesses)
    return f"""Secret word : {masked_word}
Turns remaining : {turns_remaining}
Guesses so far : {guesses}
"""
    


