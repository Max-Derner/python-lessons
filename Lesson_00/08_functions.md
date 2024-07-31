```
 _____                 _   _                 
|  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
| |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
|  _|| |_| | | | | (__| |_| | (_) | | | \__ \
|_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
```

Dead easy this one.

# Declare them
```
def my_cool_function():
    # some code
```

Want to pass in arguments?
```
def my_really_cool_function(a, b, c):
    # some code that does something with the variables a, b, and c
```
Want a default value?
```
def my_func(a='default value'):  # 
    # some stuff
```

Want to return something?
Use the keyword `return`
```
def my_useful_function():
    return "You wanted this, right?"
```

# Call them
```
my_cool_function()
```
```
my_really_cool_function(1, 'hi', True)
# Alternatively:
my_really_cool_function(b='hi', a=1, c=True)  # Note the lack of spaces around the '=', and that the arguments don't have to be in order
```
```
the_returned_value = my_useful_function()
```

### Right, consider yourselves bootstrapped! Let's get [a little challenge](./09_challenge.md) under our belts