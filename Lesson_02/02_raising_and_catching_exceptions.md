```
 ____       _     _                               _ 
|  _ \ __ _(_)___(_)_ __   __ _    __ _ _ __   __| |
| |_) / _` | / __| | '_ \ / _` |  / _` | '_ \ / _` |
|  _ < (_| | \__ \ | | | | (_| | | (_| | | | | (_| |
|_| \_\__,_|_|___/_|_| |_|\__, |  \__,_|_| |_|\__,_|
                          |___/                     
  ____      _       _     _             
 / ___|__ _| |_ ___| |__ (_)_ __   __ _ 
| |   / _` | __/ __| '_ \| | '_ \ / _` |
| |__| (_| | || (__| | | | | | | | (_| |
 \____\__,_|\__\___|_| |_|_|_| |_|\__, |
                                  |___/ 
```

# Raising Exceptions

So, raising exceptions...

Firstly, you might know this process as "throwing" an exception but round these parts we just "raise" them. Again, no one is going to care if you say you're throwing an exception instead of raising one. It's all nice and easy to do, just use the `raise` keyword and pass a little message into the initialiser, like so:

```python
raise NotImplementedError("Don't do that mate")
```

Easy! Let's see an example:
```python
class CapacityToCare:

    def __init__(self, capacity: int):
        self.capacity = capacity

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand type(s) for <: "
                F"'{type(self)}' and '{type(other)}'"
                )
        return self.capacity < other.capacity
```
Here we're guarding whether the correct type is being passed into the `__lt__` method under the `other` parameter, else we raise an exception.

# Catching Exceptions

Ok, now we're going to get into it...

## Simple catch

If you've got a bit of code that is likely to raise an exception, you pop that into a `try` block. In order to handle any exceptions raised in a try block, you handle it in an `except` block. Like this:

```python
try:
    'me' / 2
except:
    print("You can't be in two places at once!")
```
Very boring, not a lot you can do with that **and** it's against PEP8 standards to have a "bare `except`".

## Specific catch

So, the code in the above `try` block throws a specific error - the `TypeError`. Since we are now anticipating a specific error, we can catch only that error letting anything else bubble up and halt the script. Let's see that in action:

```python
try:
    'me' / 2
except TypeError:
    print("You can't be in two places at once!")
```

## Re-raising the error
Say you only want to use the except block to finish up a couple of bits before letting the script crash, like flushing out some file writes and closing those files. Well we can re-raise the error by calling a plain `raise` inside the except block, like so:

```python
# open file
file_stream = open('test.txt', mode='w')
try:
    # attempt writing into file while doing
    # dodgy stuff that might raise an error
    file_stream.write('hello\n')
    file_stream.write('trying to split self\n')
    'me' / 2
    file_stream.write('successfully split self\n')
except Exception:
    # upon catching error, gracefully flush and close the file_stream
    file_stream.flush()
    file_stream.close()
    # then re-raise the error
    raise
```


