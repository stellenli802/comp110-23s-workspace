"""LS02-04."""

__author__ = "730476572"

#LS03 (Expressions)
x: int = 1
x = x + 1
print(x) #returns 2

course: str = "110"
print(type(int(course))) #class int

from random import random
print(type(random())) #class float

from random import choice
print(type(choice("wxyz"))) #class str

print("comp110".isalpha()) #false

print("110".isdigit()) #true

print("comp110"[0].isalpha()) #true
######################################

#LS 04 (Variables and User Input)

user_name: str = input("What's your name? ")
print("Hello " + user_name + ", good morning!")
