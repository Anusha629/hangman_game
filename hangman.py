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
    


def play_round(secret_word, guesses, guess, turns_remaining):
    if guess in guesses:
        return guesses, turns_remaining, "next"
    guesses.append(guess)
    if "-" not in get_mask_word(secret_word, guesses): 
        return guesses, turns_remaining, "game_won"
    if guess not in secret_word:
        turns_remaining -= 1
        if turns_remaining == 0:
            return guesses, turns_remaining, "game_over"
    return guesses, turns_remaining, "next"



def main():
    print ("\n\n Welcome to Hangman!\n")
    secret_word = get_random_word()
    turns_remaining = 6
    guesses = []
    while True:
        status = get_status(secret_word, turns_remaining, guesses)
        print (status)
        guess = input("Enter your guess: ")
        guesses, turns_remaining, next_action = play_round(secret_word, guesses, guess, turns_remaining)
        if next_action == "game_over":
            print (f"You lost. The word is {secret_word}")
            break
        if next_action == "game_won":
            print (f"You won. The word is {secret_word}")
            break

if __name__ == "__main__":
    main()

    