```
 _   _                 _ _ _
| | | | __ _ _ __   __| | (_)_ __   __ _
| |_| |/ _` | '_ \ / _` | | | '_ \ / _` |
|  _  | (_| | | | | (_| | | | | | | (_| |
|_| |_|\__,_|_| |_|\__,_|_|_|_| |_|\__, |
                                   |___/ 
 _____                    _   _
| ____|_  _____ ___ _ __ | |_(_) ___  _ __  ___
|  _| \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \/ __|
| |___ >  < (_|  __/ |_) | |_| | (_) | | | \__ \
|_____/_/\_\___\___| .__/ \__|_|\___/|_| |_|___/
                   |_|
```

# Grappling with the exception

Say you've got some cool function that writes exceptions out to file, like this:
```python
from traceback import format_exception

EXCEPTION_FILE = 'exceptions.txt'


def exception_writer(e: Exception):
    with open(EXCEPTION_FILE, mode='a') as f:
        f.write(
            '\n'.join(format_exception(e))
        )
```
The question stands, how on Earth do you actually get the exception in order to pass it to this function.  
The answer is "with great ease". You simply add to the end of you `except` statement `as e` and then access the variable e which is the exception you're handling. You can call it something else instead of `e` but `e` is the tradition when writing python.

Example:
```python
try:
    'me'/2
except Exception as e:
    exception_writer(e)
    raise
```

# The side dishes no one talks about
So far we've seen `try` and `except` but these can be paired with `else` and/or `finally` too:
```python
try:
    # something
except:
    # handle exceptions
else:
    # stuff to do when no exception was raised
finally:
    # stuff to always do NO MATTER WHAT
```
Seems mostly reasonable, but let's dig into it a bit more and why you might decide to use the various aspects of exception handling.

So, say you're parsing some text but you also want to write logs in the worst way possible by writing to a file rather than using the [`logging` library](https://docs.python.org/3/library/logging.html) like a sensible person. You might want log something to say you're starting to parse the text, log something based on success or failure, and you may wish to always declare when you have finished. Sounds a little complex to squeeze all of that in, but it can be really nice and terse code:

```python
def parse_integer(txt: str) -> int | None:
    """Parses integers from input `txt`,
    logs to a file called `logs.txt` which will appear in the same
    directory you are running the code from"""
    with open("logs.txt", mode='a') as logs:
        logs.write("===============================\n")
        logs.write(F"Beginning to parse '{txt}'\n")
        try:
            num = int(txt)  # smallest part in try block
        except ValueError:
            logs.write("FAILED\n")  # log failure when it fails
        else:
            logs.write("SUCCESS\n")  # log success when no ValueError thrown
            return num
        finally:
            logs.write(F"Finished parse of '{txt}'\n")  # declare finished
```

This code looks like it shouldn't ever actually write "Finished parse of..." but a finally block will _**always**_ execute, even if you try to return or even perform some system exiting manuever. Having things in a `finally` block can make code less fragile as it really doesn't matter what the next coder does inside any other block, your finally block will always run no matter what.


# Placing the blame
Exceptions actually have a couple of secret attributes `__cause__` and `__context__`, and both attributes can hold extra exceptions!  
Let's look closer. Say you have a bit of code that that raises and exception and you're trying to handle it but you get all messed up and end up raising another exception. The question then comes up "Which exception do you want to see in the traceback?", the answer that Python gives is **both**.  
Take the following code for example:
```python

```