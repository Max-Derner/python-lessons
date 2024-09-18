```
 __  __             _        ____                  _           
|  \/  | __ _  __ _(_) ___  |  _ \ _   _ _ __   __| | ___ _ __ 
| |\/| |/ _` |/ _` | |/ __| | | | | | | | '_ \ / _` |/ _ \ '__|
| |  | | (_| | (_| | | (__  | |_| | |_| | | | | (_| |  __/ |   
|_|  |_|\__,_|\__, |_|\___| |____/ \__,_|_| |_|\__,_|\___|_|   
              |___/                                            
 __  __      _   _               _     
|  \/  | ___| |_| |__   ___   __| |___ 
| |\/| |/ _ \ __| '_ \ / _ \ / _` / __|
| |  | |  __/ |_| | | | (_) | (_| \__ \
|_|  |_|\___|\__|_| |_|\___/ \__,_|___/
```

So, these are more commonly called "dunder methods" (which is a contraction of double underscore methods), though they are also commonly referred to as "magic methods" (but they aren't magic, not proper magic anyway).

# What are they?
So, first off. I'm going to exclusively refer to these as dunder methods because that's what I've always known them as.  
Dunder methods basically represent all the ways to interact with a class _outside_ of dot notation. So, we've seen one already and that is `__init__`, you don't use dot notation to call this method you just issue `MyClass()`. We already know more than enough about the `__init__` method, so I will only cover it very very briefly here.

All the class dunder methods are described in [the documentation here](https://docs.python.org/3/reference/datamodel.html#special-method-names). What follows is what I consider to be the most useful dunder methods and is by no means an exhaustive list.

## `__init__(self, optional_arguments)`
This method is used to set an initial state for an instance. You should define instance variables in here using the `self` keyword.
```python
class MyClass:

    def __init__(self, some_value):
        self.some_value = some_value
        self.some_other_value = 12345
```

## `__new__(cls, optional_arguments)`
This is the method which actually creates a new object for you. This method is always called immediately prior to invocations of `__init__` without you having to manually declare it so.  
It's supposed to allow you extend from immutable objects like `int` or `tuple` or whatever. 

The only time I've seen someone use this is in creating a singleton object, like so: 

```python
class MySingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    # And then the rest of your class
```
Note that you still have to accept `*args` and `**kwargs` even though you don't do anything with them. It's a quirk, don't worry about it.

There's a lot of debate over the best way to implement a Singleton, so don't go thinking this is the only way to get singleton behaviour.

Example code has been left for you in [singleton_code.py](./section_05_supplements/singleton_code.py)

## `__str__(self)`
This is the method that gets called when you pass your instance into the built-in function `str()`. This method should return a string that gives an informal representation of the instance.

Example:
```python
class Planet:

    def __init__(self, name, x_coord, y_coord, z_coord):
        self.name = name
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def __str__(self):
        return (
            F"planet '{self.name}'"
            F" at position ({self.x}, {self.y}, {self.z})"
        )
```


```
>>> from Lesson_01.section_05_supplements.planetary_code import Planet
>>> earth = Planet('Earth', 17394, 3728943, -3272672)
>>> print(str(earth))
planet 'Earth' at position (17394, 3728943, -3272672)
```

## `__repr__(self)`
This is the method which gets run when you pass an instance into the built-in function `repr()`. This method should return a formal representation of the instance. This string should, where possible, look like the valid Python code needed to instantiate a copy of this instance.

Example:
```python
class Planet:

    def __init__(self, name, x_coord, y_coord, z_coord):
        self.name = name
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def __repr__(self):
        return (
            F"Planet(name='{self.name}', "
            F"x_coord={self.x}, "
            F"y_coord={self.y}, "
            F"z_coord={self.z})"
        )
```


```
>>> from Lesson_01.section_05_supplements.planetary_code import Planet
>>> earth = Planet('Earth', 17394, 3728943, -3272672)
>>> print(repr(earth))
Planet(name='Earth', x_coord=17394, y_coord=3728943, z_coord=-3272672)
>>> also_earth = Planet(name='Earth', x_coord=17394, y_coord=3728943, z_coord=-3272672)
>>> print(repr(also_earth))
Planet(name='Earth', x_coord=17394, y_coord=3728943, z_coord=-3272672)
```

## `__lt__(self, other)`, `__le__(self, other)`, `__eq__(self, other)`, `__ne__(self, other)`, `__gt__(self, other)`, `__ge__(self, other)`
They all map to comparison operators...

| dunder method | what? | operation |
|---------------|-------|-----------|
| `__lt__(self, other)` | less than | self < other |
| `__le__(self, other)` | less than or equal | self <= other |
| `__eq__(self, other)` | equal | self == other |
| `__ne__(self, other)` | not equal | self != other |
| `__gt__(self, other)` | greater than | self > other |
| `__ge__(self, other)` | greater than or equal | self >= other |

Example:
```python
class Planet:

    def __init__(self, name, x_coord, y_coord, z_coord):
        self.name = name
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def __lt__(self, other):
        # You need to type check and raise an error is there's an
        # incompatibility. We'll go over errors properly next lesson
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand type(s) for <: "
                F"'Planet' and '{type(other)}'"
                )
        own_distance_to_origin_squared = (
            self.x ** 2
            + self.y ** 2
            + self.z ** 2
        )
        other_distance_to_origin_squared = (
            other.x ** 2
            + other.y ** 2
            + other.z ** 2
        )

        return (
            own_distance_to_origin_squared < other_distance_to_origin_squared
        )
```
This is the crux of doing any of these dunder methods. You logic gate for compatible types, raise a `TypeError` if incompatible, get your data into a sensible form for comparison, then return that comparison. The exception to raising errors is of course in equality comparisons because if they aren't the same type, they certainly aren't going to be equal!  
Granted doing distance to origin on less than comparisons isn't the most obvious result but I wanted to keep the example class the same.

output
```
>>> from Lesson_01.section_05_supplements.planetary_code import Planet
>>> earth = Planet('Earth', 17394, 3728943, -3272672)
>>> venus = Planet('Venus', 73849050, 3487506026, -428649932)
>>> not_a_planet = "I'm not a planet!"
>>> earth < venus
True
>>> earth < not_a_planet
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/max-derner/LnD/python-lessons/zzz/sx.py", line 19, in __lt__
    raise TypeError(
TypeError: unsupported operand type(s) for <: 'Planet' and '<class 'str'>'
```


## `__hash__(self)`

This one's important if you wish to store your object in a set or as the key for a dictionary. It can feel a bit scary but it's quite simple and there's only one rule.

| **RULE 1** |
|------------|
| Objects which compare as equal, shall hash as equal! |

So, say we had constructed an `__eq__` method to only compare position since two planets can't occupy the same place but two different people might call the planets something different, like so:

```python
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        own_position = (self.x, self.y, self.z)
        other_position = (other.x, other.y, other.z)
        return own_position == other_position
```

output:
```
>>> from Lesson_01.section_05_supplements.planetary_code import Planet
>>> earth = Planet('Earth', 17394, 3728943, -3272672)
>>> not_a_planet = "I'm not a planet!"
>>> le_earth = Planet('Le Earth', 17394, 3728943, -3272672)
>>> earth == not_a_planet
False
>>> earth == le_earth
True
```

Then the hash should **_only_** encompass the values used in equality comparison. You then simply pass your values (typically as a tuple) into the `hash` built-in function, like so:
```python
    def __hash__(self):
        own_position = (self.x, self.y, self.z)
        return hash(own_position)
```

output
```
>>> from Lesson_01.section_05_supplements.planetary_code import Planet
>>> earth = Planet('Earth', 17394, 3728943, -3272672)
>>> le_earth = Planet('Le Earth', 17394, 3728943, -3272672)
>>> hash(earth)
-3483197386213214705
>>> hash(le_earth)
-3483197386213214705
```

I've left you the `Planet` in [planetary_code.py](./section_05_supplements/planetary_code.py) along with some of the example code run.

### Let's [wrap this up!](./06_closing_remarks.md)
