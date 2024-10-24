```
  ____      _   _                   ___     ____       _   _                
 / ___| ___| |_| |_ ___ _ __ ___   ( _ )   / ___|  ___| |_| |_ ___ _ __ ___ 
| |  _ / _ \ __| __/ _ \ '__/ __|  / _ \/\ \___ \ / _ \ __| __/ _ \ '__/ __|
| |_| |  __/ |_| ||  __/ |  \__ \ | (_>  <  ___) |  __/ |_| ||  __/ |  \__ \
 \____|\___|\__|\__\___|_|  |___/  \___/\/ |____/ \___|\__|\__\___|_|  |___/
```


# Getters and setters
Getters and setters go like this:

```python
class GettingAndSettingClass:

    def __init__(self, initial_value: int):
        self._my_var = initial_value

    @property
    def my_var(self):
        return self._my_var

    @my_var.setter
    def my_var(self, value):
        # isinstance() is a built-in function: https://docs.python.org/3/library/functions.html#isinstance
        if isinstance(value, int) and value >= 0:
            self._my_var = value
        else:
            print(
                "Negative value or incorrect type provided for 'my_var'"
                ", setting to 0"
            )
            self._my_var = 0
```

To note:
* We still declare the private variable (and that variable is still directly accessible)
* We declare a method in the same name as the attribute we want a **getter** for
    * this getter needs a `@property` decorator
    * this needs to be declared **_before_** we create a setter
    * this needs to actually return the value we're after
* We declare a method in the same name as the attribute we want a **setter** for
    * this setter needs a `@<variable_name>.setter` decorator
    * this needs to be declared **_after_** the getter
    * this needs to actually change the guarded variable
* We did **not** set the variable directly in in `__init__` method, we used the setter instead

Getters, setters, and even deleters are [defined here](https://docs.python.org/3/library/functions.html#property)

## Examples
Here is some sample output:
```
>>> from Lesson_01.section_04_supplements.getters_and_setters_code import GettingAndSettingClass
>>> a = GettingAndSettingClass(-1)
Negative value or incorrect type provided for 'my_var', setting to 0
>>> a.my_var = 12345
>>> a.my_var 
12345
>>> a.my_var = -12345
Negative value or incorrect type provided for 'my_var', setting to 0
>>> a.my_var
0
>>> a.my_var = "HELP!!!"
Negative value or incorrect type provided for 'my_var', setting to 0
>>> a.my_var
0
>>> 
```

The example code is left for you in [getters_and_setters_code.py](./section_04_supplements/getters_and_setters_code.py)

### That was it, let's go to [magic methods/dunder methods](./05_magic_dunder_methods.md)
