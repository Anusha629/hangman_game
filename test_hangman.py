import os
import hangman

def test_random_word_lowercase():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["Grape\n", "apple\n", "Mango\n"])
        
    for _ in range(100):
        assert hangman.get_random_word(fname) == "apple"

    os.unlink(fname)

def test_random_word_no_punctuation():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "mango's\n", '"beryl"'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"
    
    os.unlink(fname)

def test_random_word_min_length_5():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "ape\n", 'dog\n', 'bear\n'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"
        
    os.unlink(fname)

def test_random_word_no_repeated_words():
    words = {hangman.get_random_word() for _ in range(10)}
    assert len(words) == 10


def test_mask_word_no_guesses():
    guesses = []
    word = "orange"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "------"


def test_mask_word_single_correct_guess():
    guesses = ['e']
    word = "orange"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "-----e"

def test_mask_word_two_correct_guesses():
    guesses = ['o','e']
    word = "orange"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "o----e"

def test_mask_word_single_guess_multiple_occurrence():
    guesses = ['e', 'p','t']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "e-ep---t"



def test_get_status():
    secret_word = "apple"
    turns_remaining = 7
    guesses = ['x', 'p']
    status = hangman.get_status(secret_word, turns_remaining, guesses)
    expected_status = """Secret word : -pp--
Turns remaining : 7
Guesses so far : xp
"""
    assert status == expected_status

def test_play_round_correct_guess():
    secret_word = "apple"
    guesses = []
    guess = "a"
    turns_remaining = 7
    guesses, turns_remaining, next_action = hangman.play_round(secret_word, guesses,guess,turns_remaining)
    assert guesses == ['a']
    assert turns_remaining == 7
    assert next_action == "next"

def test_play_round_wrong_guess_game_not_over():
    secret_word = "apple"
    guesses = ['a']
    guess = "x"
    turns_remaining = 7
    guesses, turns_remaining, next_action = hangman.play_round(secret_word, guesses, guess, turns_remaining)
    assert guesses == ['a', 'x']
    assert turns_remaining == 6
    assert next_action == "next"

def test_play_round_wrong_guess_game_over():
    secret_word = "apple"
    guesses = ['a']
    guess = "x"
    turns_remaining = 1
    guesses, turns_remaining, next_action = hangman.play_round(secret_word,guesses, guess,turns_remaining)
    assert next_action == "game_over"