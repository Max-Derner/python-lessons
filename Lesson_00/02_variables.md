```
__     __         _       _     _           
\ \   / /_ _ _ __(_) __ _| |__ | | ___  ___ 
 \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
  \ V / (_| | |  | | (_| | |_) | |  __/\__ \
   \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
```
# Naming Variables
Variable names follow `snake_case`  
Constants are in `SCREAMING_SNAKE_CASE`  
Privates have a `_leading_underscore`

# Booleans
You've got `bool`.  
Declare it by assigning either `True` or `False`:
```
my_bool = True
```

# No value
You've got `NoneType`, it's like `null` or `void`. It's what you get when there ain't nothing to give.  
Declare it by assigning `None`:
```
my_none_type = None
```

# Numbers
## Whole numbers
You've got `int`, no long, no short, no int32.  
Declare it by assigning a number without a decimal place:
```
my_int = 1
```
If you've got a real big number, you can use an underscore as a thousands separator.  
e.g.
```
my_big_int = 1_000_000
```
## Fractions
You've got `float`, no doubles, no float64.  
Declare it by assigning a number with a decimal place:
```
my_float = 1.0
```

# Text
There's just `str`ings, there's no chars.  
Declare it by assigning something between quotes:
```
my_str = "Hello World!"
```
You can access individual characters with `my_str[2]` but cannot assign values in this way (i.e. `my_str[2] = 'd'` doesn't work)


# Collections
_QUICK NOTE:_ Any of the objects under this section (and strings as it happens) can have their length checked by passing them into the `len()` function.  
_SECOND QUICK NOTE:_ These objects can't be copied with `my_copy = your_copy`, it has to be `my_copy = your_copy.copy()` but this is only a shallow copy, deep copies will come in a later lesson.  


## Key-Value Pairs `dict`
We call them `dict`ionaries, you might call them dictionaries, hash-maps, hash-tables.  
Declare it by assigning some comma separated key-value pairs between braces, a key must be separated from a value by a colon:
```
my_dict = {'key': 'value', 'a': 1, 1: 'one'}
```
Dictionaries don't have a fixed length, and can contain any mix of types for both keys and values.  
Keys must be unique.  
Access a value with `my_dict['key']`.  
Check if a key exists with `my_key in my_dict` (expression returns True if it exists in dict)  
Add a value with `my_dict['new_key'] = 'new value'` (if `'new_key'` already exists in the dictionary, then you will overwrite the previous value)  
To remove a key-pair from a dictionary it's `del my_dict['key to delete']`  
To get a list of keys it's `my_dict.keys()` and a list of values is `my_dict.values()`.  


## Value only with duplicates `list`
There's only `list`, no arrays, no vectors.  
Declare it by assigning some comma separated values between square brackets:
```
my_list = [1, 2, 'c', 'd']
```
Lists don't have a fixed length, and can contain any mix of types.  
Access individual elements with `my_list[3]` and assign them the same way.  
Add to a list with `my_list.append(my_int)`  
Remove an element at a specific index with `del my_list[3]`  
If you only know the value, you can remove that element with `my_list.remove(stored_value)` if there are multiple instances of this value it will only remove the first.  
Sort lists with `my_list.sort()` (this mutates the list itself, it doesn't return anything)  
Reverse a list with `my_list.reverse()` (this also mutates the list itself and doesn't return anything)  


## Value only without duplicates `set`
We call this a `set`.  
Declare it by assigning some comma separated values between braces:
```
my_set = {1, 2, 'c', 'd'}
```
Sets don't have a fixed length, and can contain a mix of types (so long as their hashable but we'll get to that later).  
Sets don't maintain order, so you can't access a specific element.  
Add to a set with `my_set.add(my_int)`  
Check if something is in a set with `my_int in my_set` (expression returns True if it exists in set)  
Remove something from a set with `my_set.discard(my_int)`


## Immutable value only with duplicates `tuple`
We call this a `tuple`.  
Declare it by assigning some comma separated values between parentheses:
```
my_tuple = (1, 'two', 3)
```
Tuples can contain any mix of types.  
You can't add to, or remove from a tuple because it's immutable.  
You can access a specific element with `my_tuple[2]`.  
Check if something is in a tuple with `my_int in my_tuple` (expression returns True if it exists in tuple)  

They might seem a little bloody useless, but I promise they enable some cool stuff that we'll get to later.

# Truthy/Falsy
There are truthy/falsy values in Python. Everything is truthy unless it's; zero, None, False, or empty.


# That's it?
Yeah, for now.
### [Moving on!](./03_comments.md)

