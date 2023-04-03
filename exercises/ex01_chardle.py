"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730476572"

# Sets up variables
five_character: str = input("Enter a 5-character word: ")
single_character: str = input("Enter a single character: ")

if (len(five_character) != 5):
    print("Error: Word must contain 5 characters.")
    exit()
elif (len(single_character) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_character)

index: int = 0
count: int = 0
result: str = str(index)
if (single_character == five_character[0]):
    print(single_character + " found at index " + str(index))
    count = count + 1
index = index + 1
if (single_character == five_character[1]):
    print(single_character + " found at index " + str(index))
    count = count + 1
index = index + 1
if (single_character == five_character[2]):
    print(single_character + " found at index " + str(index))
    count = count + 1
index = index + 1
if (single_character == five_character[3]):
    print(single_character + " found at index " + str(index))
    count = count + 1
index = index + 1
if (single_character == five_character[4]):
    print(single_character + " found at index " + str(index))
    count = count + 1
index = index + 1
if (count == 0):
    print("No instances of " + single_character + " found in " + five_character)
elif (count == 1):
    print(str(count) + " instance of " + single_character + " found in " + five_character)
else:
    print(str(count) + " instances of " + single_character + " found in " + five_character)