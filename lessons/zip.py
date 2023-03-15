"""CQ_04: Dict function writing."""

__author__ = "730476572"

def zip(a: list[str], b: list[int]) -> dict[str, int]:
    """Return a dict with the keys in list a and values in list b."""
    output: dict[str, int] = dict()
    # return empty dict if input lists are different lengths or empty
    if (len(a) == 0 and len(b) == 0):
        return output
    elif (len(a) != len(b)):
        return output
    #  return a dict with keys in list a and values in list b
    else:
        for i in len(a):
            output = {a[i]: b[i]}
    return output
