"""ex07-Dictionary Test."""
__author__ = "730476572"

import pytest
from exercises.ex07.dictionary import invert, favorite_color, count

with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_edge() -> None:
    """Edge case to test for empty dictionary."""
    assert invert({}) == {}


def test_invert_use1() -> None:
    """Use case 1."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use2() -> None:
    """Use case 2."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_favorite_color_edge() -> None:
    """Edge case to test for empty dicionary."""
    assert favorite_color({}) == []


def test_favorite_color_use1() -> None:
    """Use case 1 to test for general functionality."""
    assert favorite_color({"one": "blue", "two": "blue", "three": "blue", "four": "yellow"}) == "blue"


def test_favorite_color_use2() -> None:
    """Use case 2 to test when the two colors appear the same number of times."""
    assert favorite_color({"ste": "yellow", "ce": "yellow", "l": "blue", "kk": "blue"}) == "yellow"


def test_count_edge() -> None:
    """Edge case to test for empty list."""
    assert count([]) == {}


def test_count_use1() -> None:
    """Use case 1 to test for general functionality."""
    assert count(["three", "three", "three", "one"]) == {"three": 3, "one": 1}


def test_count_use2() -> None:
    """Use case 2 to test."""
    assert count(["one", "1", "ONE"]) == {"one": 1, "1": 1, "ONE": 1}