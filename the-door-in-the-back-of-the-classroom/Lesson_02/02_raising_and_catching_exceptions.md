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

Firstly, you might know this process as "throwing an error" but round these parts we "raise exceptions" them. Again, no one is going to care if you say you're throwing an error instead of raising an exception. It's all nice and easy to do too, just use the `raise` keyword and pass a little message into the initialiser, like so:

```python
raise NotImplementedError("You'll need to actually write something for this")
```

Easy! Let's see an example:
```python
def positive_number_gate(item):
    if not (
        isinstance(item, int)
        or isinstance(item, float)
    ):
        raise TypeError(F"item: {repr(item)} is not an int of float")
    if item < 0:
        raise ValueError(F"item: {repr(item)} is not a positive number")
```
Here we're guarding whether the correct type is being used, and whether it is an appropriate value. You can see the [code in `number_gate.py`](./section_02_supplements/number_gate.py)

# Catching Exceptions

Well raising exceptions was never going to be the hard part, was it?

## Simple catch

If you've got something that's liable to raise an exception, pop it into a `try` block. In order to handle any exceptions raised in a try block, you handle it in an `except` block.  
Like this:

```python
try:
    positive_number_gate("I ain't no number!")
except:
    print("Whoops! Something has gone wrong!")
```
[code in `bare_except.py`](./section_02_supplements/bare_except.py)  
Very boring, not a lot you can do with that **and** it's against PEP8 standards to have a "bare `except`".

**N.B.** You cannot have a lone `try` block, you _must_ pair it with an `except` block!  
Instead, you should use:
```python
except Exception:
```
This line will not only catch the `Exception` exception, but also catch any exception which inherits from `Exception` (which is all of the none system exiting exceptions as we heard earlier)

## Specific catch

So, the code in the above `try` block throws a specific error - the `TypeError`. Since we are now anticipating a specific error, we can catch only that error letting anything else bubble up and halt the script. Let's see that in action:

```python
try:
    positive_number_gate("I ain't no number!")
except TypeError:
    print("Whoops! That wasn't a number")
```
[code in `specific_except.py`](./section_02_supplements/specific_except.py)

## Catching Multiple Specific Exceptions
Ok, but our code could throw a couple of different exceptions. The above is great if we can guarantee only `TypeError`s, but fact of the matter is we might end up with a `ValueError` too!  
We can handle both the same way like this:
```python
try:
    positive_number_gate(item)
    print("Hey! That was a good number")
except (TypeError, ValueError):
    print("Ooops! Something went wrong there!")
```
[code in `multiple_except.py`](./section_02_supplements/multiple_except.py)


## Unique Handling for Exceptions
Well what if you want to handle these things separately? You can chain `except` blocks together to act on the same `try` block like this:
```python
try:
    positive_number_gate(item)
    print("Hey! That was a good number")
except TypeError:
    print("Ooops! That wasn't a number")
except ValueError:
    print("Ooops! That was a bad number")
```
[code in `multiple_except_diverse_handling.py`](./section_02_supplements/multiple_except_diverse_handling.py)

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
    positive_number_gate("I ain't no number!")
    file_stream.write('successfully split self\n')
except Exception:
    # upon catching error, gracefully flush and close the file_stream
    file_stream.flush()
    file_stream.close()
    # then re-raise the error
    raise
```

# Quick Tip

When working with a `try`/`except` blocks, be sure to place as little as possible within the `except` block.


# [Let's look at how to format the exception now we can handle it](./03_exception_formatting.md)

