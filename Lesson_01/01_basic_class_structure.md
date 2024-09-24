```
 ____            _         ____ _               
| __ )  __ _ ___(_) ___   / ___| | __ _ ___ ___ 
|  _ \ / _` / __| |/ __| | |   | |/ _` / __/ __|
| |_) | (_| \__ \ | (__  | |___| | (_| \__ \__ \
|____/ \__,_|___/_|\___|  \____|_|\__,_|___/___/
```

# The basic class

```python
class Basic:

    def __init__(self, value: int):
        self.value = value

    def some_method(self, multiplicant: int) -> int:
        print("I'm doing stuff")
        return self.value * multiplicant
```
Few things to note:
* We declare our class using the keyword `class`
* Our classes are named in CamelCase
* The initialising function is called `__init__` (note the two underscores either side)
* `self` acts as the variable to refer to the instance of the class itself
* `self` must be the first argument passed into any method belonging to a class

**N.B.** you don't _have_ to call the `self` keyword "self". If you replaced every instance of `self` with `this` (like the Java equivalent) nothing bad would happen, it's not even a PEP8 standard! I say nothing bad would happen, but your Python fanatic colleagues would secretly hate you forever because naming it "self" is standard procedure.


# Privates, constants, default arguments, and docstrings
```python
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
```
[Counter code is here](./section_01_supplements/counter_code.py)  

Note:
* both private methods and private variables are named with a leading underscore.  
* constants are declared in `SCREAMING_SNAKE_CASE`
* a default value for an argument is declared with `=` in the method signature
    * Do be careful with default values, default values should never be mutable else you will get unexpected results. [See example](./section_01_supplements/default_args_example.md)
* docstrings are
    * declared as a string with 3 times the number of double quotes a regular sting is
    * declared immediately beneath either the class signature or method signatures
    * what shows up when hovering over the class initialisation or method call in the IDE
    * roughly following markdown (you still can't have trailing spaces though because of PEP8)
**N.B.** Remember that private functions and variables can both still be accessed from outside the class, and constants can still be changed. The interpreter is not going to stop you from doing either (which is actually handy for testing)

[Next section, inheritance!](./02_inheritance.md)