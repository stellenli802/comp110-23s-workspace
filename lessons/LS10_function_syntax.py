"""Example functions to learn defining and calling syntax"""

def my_max(num1: int, num2: int) -> int:
    """Returns the max value out of 2 given integers"""
    if(num1 >= num2):
        return num1 
    else:
        return num2

# calling function
max_num: int = my_max(4,9)
print(max_num)

def hello_n(n: int) -> int:
   """A silly example function."""
   return "hello " + str(n)

print(hello_n(3))