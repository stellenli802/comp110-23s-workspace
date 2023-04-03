"""Practice importing from other modules."""

from lessons import LS14a_my_function
#OR
#from lessons.LS14a_my_function import addition

#print(LS14a_my_function.addition(4,2))
#print(LS14a_my_function.my_variable)

if __name__ == "__main__":
    print("Howdy!")