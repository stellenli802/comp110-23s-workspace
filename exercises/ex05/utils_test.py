"""Ex05-Utility functions test."""
__author__ = "730476572"


from exercises.ex05.utils import only_evens, sub, concat

# 1 edge case and 2 use cases for only_evens()
def test_only_evens_empty() -> None:
    assert only_evens([]) == []

def test_only_evens_use1() -> None:
    assert only_evens([1, 3, 5]) == []

def test_only_evens_use2() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


# cases for concat()
def test_concat_empty() -> None:
    assert concat([], []) == []

def test_concat_use1() -> None:
    assert concat([1, 3, 9, 3], []) == [1, 3, 9, 3]

def test_concat_use2() -> None:
    assert concat([], [3, 3, 3, 9]) == [3, 3, 3, 9]

def test_concat_use3() -> None:
    assert concat([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


# cases for sub()
def test_sub_empty() -> None:
    # empty if length of the list is 0
    assert sub([], 1, 2) == []
    # empty if start is greater than or equal to the length of the list
    assert sub([1, 2, 3, 4, 5], 9, 3) == []
    # empty if end is at most 0
    assert sub([1, 2, 3, 4, 5], 1, 0) == []

def test_sub_case1() -> None:
    # start from the beginning of the list if start is negative
    assert sub([1, 2, 3, 4, 5], -3, 2) == [1, 2]
    # end with the end of the list if end is greater than the length of the list
    assert sub([1, 2, 3, 4, 5], 3, 9) == [4, 5]

def test_sub_case2() -> None:
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]