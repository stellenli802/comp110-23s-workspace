"""ex03_wordle."""

__author__ = "730476572"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, single_char: str) -> bool:
    """Function to check if a letter is contained within the string/secret word."""
    assert len(single_char) == 1
    ind: int = 0
    # True if char exists in word, False otherwise
    while (ind < len(word)):
        if (single_char == word[ind]):
            return True
        else:
            ind = ind + 1
    return False


def emojified(guess: str, word: str) -> str:
    """Function that returns colored boxes for two equal-length strings."""
    assert len(guess) == len(word)
    ind: int = 0
    results: str = ""
    # green box if same letter same position, yellow only if the word contains the letter
    while (ind < len(guess)):
        if (contains_char(word, guess[ind]) is True):
            if (word[ind] == guess[ind]):
                results += GREEN_BOX
            else:
                results += YELLOW_BOX
        else:
            results += WHITE_BOX
        ind = ind + 1
    return results


def input_guess(length:int) -> str: 
    """Function that makes sure user's input is correct length with the secret word."""
    guess = input(f"Enter a { length } character word: ")
    while (len(guess) != length):
        new_guess = input(f"That wasn't { length } chars! Try again: ")
        guess = new_guess
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # defining the 'state' of the game
    # max. num. of guesses per game
    max: int = 6
    # current turn number
    turns: int = 1
    word: str = "codes"
    while (turns <= max):
        print(f"=== Turn { turns }/ { max } ===")
        # prompts input for the guess
        guess = input_guess(len(word))
        # results for that guess
        results = emojified(guess, word)
        print(results)
        # terminate while loop if guessed correcrly
        if (results == len(word) * GREEN_BOX):
            print(f"You won in { turns }/ { max } turns! ")
            max = 0
        else: 
            turns = turns + 1
    if (max != 0):
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()