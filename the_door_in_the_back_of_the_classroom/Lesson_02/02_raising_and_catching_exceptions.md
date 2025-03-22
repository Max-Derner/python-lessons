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

Firstly, you might know this process as "_throwing an error_" but in Python parlance it's actually "_raising an exception_". No one really cares though, so call it what you want. Anyway, it's all nice and easy to do, just use the `raise` keyword and pass a little message into the initialiser, like so:

```python
raise NotImplementedError("You'll need to actually implement this")
```

Easy! Let's see an example:
```python
def positive_number_gate(item):
    if not (
        isinstance(item, int)
        or isinstance(item, float)
    ):
        raise TypeError(F"item: {repr(item)} is not an int or float")
    if item < 0:
        raise ValueError(F"item: {repr(item)} is not a positive number")
```
Here we're guarding whether the correct type is being used, and whether it is an appropriate value. You can see the [code in `number_gate.py`](./raising_and_catching_supplements/number_gate.py)

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
[code in `bare_except.py`](./raising_and_catching_supplements/bare_except.py)  
Very boring, not a lot you can do with that **and** it's against PEP8 standards to have a "bare `except`". Instead, you should use:
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
[code in `specific_except.py`](./raising_and_catching_supplements/specific_except.py)

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
[code in `multiple_except.py`](./raising_and_catching_supplements/multiple_except.py)


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
[code in `multiple_except_diverse_handling.py`](./raising_and_catching_supplements/multiple_except_diverse_handling.py)

## Re-raising the error
Say you're writing some logs to a file instead of using a file handler on a logger from the [`logging` library](https://docs.python.org/3/library/logging.html) (something we will cover in a future lesson). And you both want to be able to log that an exception has occurred and allow it to bubble up and halt the system. Well, it is possible to re-raise an exception after you have caught it.

```python
nums_to_sum = [1, 10, 100, "1", 42, 999]

with open("logs.txt", mode='w') as logs:  # get our log file going
    try:
        # do a bunch of stuff
        logs.write(F"Starting work at {datetime.now()}\n")
        a = 0
        nums_summed = 0
        for num in nums_to_sum:
            logs.write(F"Adding {num=}, {nums_summed=}\n")
            a += num
            nums_summed += 1
        logs.write("Finished work successfully\n")
    except Exception:
        # if anything goes wrong, write that to file
        logs.write(F"Failed work after summing {nums_summed} nums\n")
        raise  # get that exception back out in the wild
```
[code in `re_raise.py`](./raising_and_catching_supplements/re_raise.py)

Ok, so let's run with that for a while but let's say we can't halt the system here, instead we need to keep going regardless and just note down the issue for 3rd line support to pick up. This code currently just says that something went wrong but it doesn't highlight what exactly it was that happened. So how do we go about doing that? Well, you can access the exception object once it's been caught by aliasing the exception like you do when importing a module.

Let's go with a different example for now though...

```python
    some_dict = {
        'a': 'apple',
        'bee': 'buzz',
        'c': 'carrot',
    }

    for key in ['a', 'b', 'c']:
        try:
            print(F"{key} is for {some_dict[key]}")
        except Exception as e:  # aliasing exception here
            print("EXCEPTION!")
            print(e)  # printing it here
```
So here, you can see that you're calling the exception `e` and then printing it out a short while later.  
[code is here](./raising_and_catching_supplements/aliasing_exception.py) try running it though and you will immediately see a problem.

## Formatting exceptions
Did you run that last bit of code? No? Well I couldn't be more disappointed in you. Anyway, if you did, it would've looked like this:
```
a is for apple
EXCEPTION!
'b'
c is for carrot
```
That's right, all that printed out is `'b'`! Because that's the message you get on a `KeyError` like that, you only get the key you tried to use. If you didn't just print it out and instead used the `repr()` function you'd at least get the class of exception too: `KeyError('b')`. But there is a whole module for this exact thing, the [`traceback` module](https://docs.python.org/3/library/traceback.html).

Now, if we go back to our original example of writing logs we can add the traceback module and see how it works.

```python
from datetime import datetime
from traceback import format_exception


nums_to_sum = [1, 10, 100, "1", 42, 999]

with open("logs.txt", mode='w') as logs:  # get our log file going
    try:
        # do a bunch of stuff
        logs.write(F"Starting work at {datetime.now()}\n")
        a = 0
        nums_summed = 0
        for num in nums_to_sum:
            logs.write(F"Adding {num=}, {nums_summed=}\n")
            a += num
            nums_summed += 1
        logs.write("Finished work successfully\n")
    except Exception as e:
        # if anything goes wrong, write that to file
        logs.write(F"Failed work after summing {nums_summed} nums\n")
        logs.write("EXCEPTION:\n")
        logs.write(format_exception(e))

```
Now `format_exception()` will format the exception to look exactly the same as when it halts the system.  
[code available here](./raising_and_catching_supplements/formatting_exceptions.py)

# Quick Tip

When working with a `try`/`except` blocks, be sure to place as little as possible within the `try` block. The above example is **not** a best practice.


### [Let's look at how best to handle exceptions](./03_handling_exceptions.md)

