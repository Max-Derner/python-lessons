

# Make sue you hover over all the different class and method uses here
# to look at the way that the docstrings are formatted


class Counter:
    """A counter with overflow.

    If a limit is specified and then exceeded, the count will be
    reset to starting value."""

    def __init__(self, starting_value: int, limit: int | None = None):
        # private attribute
        self._count = starting_value
        # constant attributes
        self.STARTING_VALUE = starting_value
        self.LIMIT = limit

    def view_count(self) -> int:
        """returns the current count _without_ incrementing it"""
        return self._count

    def count(self) -> int:
        """increments count and returns it"""
        self._increment_count()
        return self._count

    def _increment_count(self):
        """a private method to:

        * securely increment the count
        * safely overflow in case of limits"""
        if self.LIMIT is not None and self._count == self.LIMIT:
            self._count = self.STARTING_VALUE
        self._count += 1


if __name__ == "__main__":
    my_counter = Counter(0)
    print(my_counter.view_count())
    print(my_counter.count())
