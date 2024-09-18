## [<- GO BACK](../01_basic_class_structure.md#privates-constants-default-arguments-and-docstrings)


### **N.B.** This wisdom applies to default arguments being used in function signatures as well as class method signatures.  

# How does this happen?

When a module is imported, the interpreter runs over the function signature and sets the default value for the argument at that point in time.  

**N.B.** Once a module has been run over by the interpreter it goes into `sys.modules` as an initialised module object, if you then import it again the pre-initialised object is fetched from `sys.modules`, meaning that the values won't be reset.  

When the function is invoked, this pre-initialised argument gets passed in and the variable that is used inside your function is now name shadowing the argument in a different scope. So for immutable types, when you change the value of your variable inside the function it now has to use a different object and so the name shadowed variable points to a different object. However, when that object is mutable there's no need for your name shadowed variable to point to a new object since the object can be changed in place. This results in the new value being reflected in the default argument being passed in, which has knock-on effects for future invocations.

For what you'll see on a daily basis, there are only the three mutable types to worry about: `dict`, `list`, and `set`.


# Example of when things go wrong
Say we define these two functions (again, the same wisdom holds for class methods):
```python
# mutable default
def add_to_list(value, list_to_add_to: list = []):
    list_to_add_to.append(value)
    return list_to_add_to


# immutable default
def add_to_number(value, number_to_add_to: int = 0):
    number_to_add_to += value
    return number_to_add_to
```
Note:
* both `add_to_list` and `add_to_number` have default values declared for one of their arguments
* `add_to_list` has a default value which is mutable
* other than the mutability, these are essentially the exact same function

Example use:
```
>>> from Lesson_01.section_01_supplements.bad_args_code import add_to_list
>>> add_to_list(1)
[1]
>>> add_to_list(1)
[1, 1]
>>> add_to_list(1)
[1, 1, 1]
>>> add_to_list(1, [3, 2])
[3, 2, 1]
>>> add_to_list(1)
[1, 1, 1, 1]
```

You can see that despite it appearing as though we should be getting a fresh empty list each time, we are actually adding to the object which our default argument points to since it is mutable.  

If we do the same thing with the other function, we get:
```
>>> from Lesson_01.section_01_supplements.bad_args_code import add_to_number
>>> add_to_number(1)
1
>>> add_to_number(1)
1
>>> add_to_number(1)
1
>>> add_to_number(1, 5)
6
>>> add_to_number(1)
1
```

You can see here that since the object which our default argument is pointing to is mutable, we don't have the same issue.

# So how do we fix the problem?

You simply detect a default state and reassign a new object inside the class. You could do that by detecting an empty list and reassigning your name shadowing internal variable to a brand new list but the method signature will confuse anyone who knows about this quirk of Python.

So, the Pythonic way is to give it a default value of None and detect that, like so:
```python
# immutable default
def add_to_list_v2(value, list_to_add_to: list | None = None):
    if list_to_add_to is None:
        list_to_add_to = []
    list_to_add_to.append(value)
    return list_to_add_to
```

Since `None` is an immutable object we are now protected from the previous issue since reassignment causes the name shadowing internal variable to point to a new object, and when we reassign the value we are creating a brand new object every time.

Example use:
```
>>> from Lesson_01.section_01_supplements.bad_args_code import add_to_list_v2
>>> add_to_list_v2(1)
[1]
>>> add_to_list_v2(1)
[1]
>>> add_to_list_v2(1)
[1]
>>> add_to_list_v2(1, [3, 2])
[3, 2, 1]
>>> add_to_list_v2(1)
[1]
```

## The code shown on this page has been left for you in [bad_args_code.py](./bad_args_code.py)

## [<- GO BACK](../01_basic_class_structure.md#privates-constants-default-arguments-and-docstrings)