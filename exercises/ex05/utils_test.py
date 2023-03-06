"""Ex05-Utility functions test."""
__author__ = "730476572"


from exercises.ex05.utils import only_evens, sub, concat

# 1 edge case and 2 use cases for only_evens()
def test_only_evens_empty() -> None:
    """Test the output if input list is empty."""
    assert only_evens([]) == []


def test_only_evens_use1() -> None:
    """Test the output if input list has only odds."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_use2() -> None:
    """Test the output for a mixed input list."""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


# cases for concat()
def test_concat_empty() -> None:
    """Test the concat() function when both given lists are empty."""
    assert concat([], []) == []


def test_concat_use1() -> None:
    """Test the output when the second given list is empty."""
    assert concat([1, 3, 9, 3], []) == [1, 3, 9, 3]


def test_concat_use2() -> None:
    """Test the output when the first given list is empty."""
    assert concat([], [3, 3, 3, 9]) == [3, 3, 3, 9]


def test_concat_use3() -> None:
    """Test the output with a use case."""
    assert concat([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


# cases for sub()
def test_sub_empty() -> None:
    """Test the sub() function with three possible scenarios to get an empty list as the result."""
    # empty if length of the list is 0
    assert sub([], 1, 2) == []
    # empty if start is greater than or equal to the length of the list
    assert sub([1, 2, 3, 4, 5], 9, 3) == []
    # empty if end is at most 0
    assert sub([1, 2, 3, 4, 5], 1, 0) == []


def test_sub_case1() -> None:
    """Test the output when either the start is negative or when the end is greater than the length of the list."""
    # start from the beginning of the list if start is negative
    assert sub([1, 2, 3, 4, 5], -3, 2) == [1, 2]
    # end with the end of the list if end is greater than the length of the list
    assert sub([1, 2, 3, 4, 5], 3, 9) == [4, 5]


def test_sub_case2() -> None:
    """Test the output with a use case."""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]