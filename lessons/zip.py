"""CQ_04: Dict function writing."""

__author__ = "730476572"

def zip(key: list[str], value: list[int]) -> dict[str, int]:
    """Return a dict with the keys in list a and values in list b."""
    output: dict[str, int] = {}
    # return empty dict if input lists are different lengths or empty
    if (len(key) != len(value)):
        return output
    #  return a dict with keys in list a and values in list b
    else:
        for i in range(len(key)):
            output[key[i]] = value[i]
    return output
