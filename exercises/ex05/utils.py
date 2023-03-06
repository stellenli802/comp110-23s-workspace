"""Ex05-Utility functions."""
__author__ = "730476572"


def only_evens(a: list[int]) -> list[int]:
    """Given a list of integers, return a list with only even values from that given list"""
    output: list[int] = []
    for i in a:
        if i % 2 == 0:
            output.append(i)
    return output

def concat(a: list[int], b: list[int]) -> list[int]:
    """Given two lists of integers, return a list that contains all elements from both lists"""
    output: list[int] = []
    # append all elements from list 1 to the output list
    for i in a: 
        output.append(i)
    # append all elements from list 2 to the output list
    for i in b:
        output.append(i)
    return output

def sub(list: list[int], start: int, end: int):
    output: list[int] = []
    # return empty list if the length of the list is 0, 
    # start is greater than or equal to the length of the list, or end is at most 0
    if len(list) == 0 or start >= len(list) or end <= 0:
        return output
    # if the start index is negative, start from the beginning of the list 
    # if the end index is greater than the length of the list, end with the end of the list
    if start < 0:
        start = 0
        for i in range(start, end):
            output.append(list[i])
    elif end > len(list):
        for i in range(start, len(list)):
            output.append(list[i])
    else:
        for i in range(start, end):
            output.append(list[i])
    return output