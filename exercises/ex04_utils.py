"""ex04_'list' Utility Functions."""

__author__ = "730476572"

def all(a: list[int], b: int) -> bool:
    """Returns True if all the ints in the list are same as the given int, False otherwise or if empty list."""
    ind: int = 0
    if (len(a) == 0):
        return False
    while (ind < len(a)):
        if (a[ind] != b):
            return False
        ind += 1
    return True


def max(input: list[int]) -> int:
    """Given a list of ints, return the largest in the List."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    val: int = input[0]
    while (i < len(input)):
        if (input[i] > val):
            val = input[i]
        i += 1
    return val
        

def is_equal(c: list[int], d: list[int]) -> bool:
    """Returns True if lists are equal, False otherwise."""
    if len(c) != len(d):
        return False
    i: int = 0
    while i < len(c):
        if c[i] != d[i]:
            return False
        i += 1
    return True