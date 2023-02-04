"""EX02 - One-Shot Wordle"""

__author__ = "730476572"

#initiates variables
secret: str = "python"
guess: str = input(f"What is your { len(secret) }-letter guess? ")
new_guess: str = " "
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


#while-loop to check for length of input
while(len(guess) != len(secret)):
    new_guess = input(f"That was not { len(secret)} letters ! Try again: ")
    guess = new_guess

#initialize checking variables 
index: int = 0
result: str = ""


#while-loop to check each index of the guess with the secret word
while(index < len(secret)):
    #green if same letter at same index
    if(guess[index] == secret[index]):
        result += GREEN_BOX
    else:
        in_word: bool = False
        alt_index: int = 0
        #while-loop to check if the letter is in the word at all
        while(in_word == False and alt_index < len(secret)):
            if(guess[index] == secret[alt_index]):
                in_word = True
            else:
                alt_index = alt_index + 1
        if(in_word == True):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    index = index + 1
print(result)

if(guess != secret):
    print("Not quite. Play again soon! ")
else:
    print("Woo! You got it!")

