

def positive_number_gate(item):
    if not (
        isinstance(item, int)
        or isinstance(item, float)
    ):
        raise TypeError(F"item: {repr(item)} is not an int or float")
    if item < 0:
        raise ValueError(F"item: {repr(item)} is not a positive number")
