"""ex07-Dictionary."""
__author__ = "730476572"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values."""
    output: dict[str, str] = {}
    key: list[str] = []
    value: list[str] = []
    # puts the keys and values into two separate lists
    for elem in input:
        key.append(elem)
        value.append(input[elem])
    # check for duplicates in the values/keys of the inverted dictionary
    for elem in value:
        if value.count(elem) > 1:
            raise KeyError(f"KeyError: {elem} already exists in the inverted dictionary")
    # goes through the dictionary and inverts the keys and the values
    for idx in range(len(input)):
        output[value[idx]] = key[idx]
    return (output)


def favorite_color(input: dict[str, str]) -> str:
    """Finds the color that appears the most in a dictionary."""
    colors: list[str] = []
    # puts all the values/colors into a list
    for elem in input:
        colors.append(input[elem])
    if colors == []:
        return (colors)
    return (max(colors, key=colors.count))


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of apperances of each element in the list."""
    output: dict[str, int] = {}
    # loop through the items in the input list
    for elem in input:
        if elem in output:
            output[elem] += 1
        else:
            output[elem] = 1
    return output
