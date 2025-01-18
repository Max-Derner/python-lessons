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

Say you've got some function that writes exceptions out to file, like this:
```python
def exception_writer(e: Exception):
    with open('exceptions.txt', mode='a') as f:
        f.write(repr(e))
```
The question stands, how on Earth do you actually get the exception in order to pass it to this function.  
The answer is "with great ease". You simply add to the end of you `except` statement `as e` and then access the variable `e` which is the exception you're handling. You can call it something else instead of `e` but `e` is the tradition when writing Python.

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
    # stuff to always do NO MATTER WHAT, including if a system exiting
    #  exception is raised or you try to exit the code with the exit()
    # function.
```
Seems mostly reasonable, but let's dig into it a bit more and why you might decide to use the various aspects of exception handling.

So, say you're parsing some text but you're still writing logs in the worst way possible by writing to a file rather than using the [`logging` library](https://docs.python.org/3/library/logging.html). You might want log something to say you're starting to parse the text, log something based on success or failure, and you may wish to always declare when you have finished. Sounds a little complex to squeeze all of that in, but it can be really nice and terse code:

```python
def parse_integer(txt: str) -> int | None:
    """Parses integers from input `txt`,
    logs to a file called `logs.txt` which will appear in the same
    directory you are running the code from"""
    with open("logs.txt", mode='a') as logs:
        logs.write("===============================\n")
        logs.write(F"Beginning to parse '{txt}'\n")
        try:
            # smallest part in try block
            num = int(txt)
        # ValueError is all that should be raised when
        #  failing a type cast
        except ValueError:
            # log failure when it fails
            logs.write("FAILED\n")
        else:
            # log success when no ValueError thrown
            logs.write("SUCCESS\n")
            # return your value over here in the success block
            return num
        finally:
            # declare finished, this will actually intercept the return
            #  statement above
            logs.write(F"Finished parse of '{txt}'\n")
```
[Code here](./handling_exception_supplements/integer_parse.py)

This code looks like it shouldn't ever actually write "Finished parse of..." but a finally block will _**always**_ execute, even if you try to return or even perform some system exiting manuever. Having things in a `finally` block can make code less fragile as it really doesn't matter what the next coder does inside any other block, your finally block will always run no matter what.


# Placing the blame
Exceptions actually have a couple of secret attributes `__cause__` and `__context__`, and both attributes can hold extra exceptions!  
Let's look closer. Say you have a bit of code that raises an exception and you're trying to handle it but you get all messed up and end up raising another exception. The question then comes up "Which exception do you want to see in the traceback?", the answer that Python gives is **both**.  
Take the following code for example:
```python
try:
    float('me')
except Exception as e:
    'you' ** 'python lessons'
```
What you get is a traceback like this:
```
Traceback (most recent call last):
  File "<python-input-4>", line 2, in <module>
    float('me')
    ~~~~~^^^^^^
ValueError: could not convert string to float: 'me'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<python-input-4>", line 4, in <module>
    'you' ** 'python lessons'
    ~~~~~~^^~~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
```
You essentially get the first exception printed out, a line reading "`During handling of the above exception, another exception occurred:`", and then the second exception. This lets you know what initially went wrong and then what went wrong while trying to handle that issue.

So, what's happened is that we've `try`ed `float('me')` and ended up with a `ValueError`. This has then been `except`ed and we've then raised you to the power of python lessons with `'you' ** 'python lessons'`. This has then caused a `TypeError`, that exception has had the original `ValueError` assigned as the `.__context__`. Now Python raises the new `TypeError` which outputs both the `ValueError` we were originally trying to deal with and the new `TypeError` which we caused while trying to handle the first exception.

**But**, there are times when you might be trying to get something done and an exception prevents you from doing so. In this case you may need to raise a custom exception that's easy enough to catch whilst also placing the blame on what underlying thing has gone wrong. In this case, we use the `from` keyword:

```python
class SumError(Exception):
    """raised when custom_sum fails"""


def custom_sum(nums: list[int | str]) -> int | None:
    sum = 0
    for num in nums:
        try:
            sum += int(num)
        except ValueError as e:
            raise SumError from e
    return sum
```
[find code here](./handling_exception_supplements/from_demo.py)  

With the following main guard clause:   
```python
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 'five', 6]
    custom_sum(nums)
```

You get the following stacktrace:  
```
Traceback (most recent call last):
  File "/home/maxwell/Programming/Python/python-lessons/the-door-in-the-back-of-the-classroom/Lesson_02/handling_exception_supplements/from_demo.py", line 11, in custom_sum
    sum += int(num)
           ~~~^^^^^
ValueError: invalid literal for int() with base 10: 'five'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/maxwell/Programming/Python/python-lessons/the-door-in-the-back-of-the-classroom/Lesson_02/handling_exception_supplements/from_demo.py", line 19, in <module>
    custom_sum(nums)
    ~~~~~~~~~~^^^^^^
  File "/home/maxwell/Programming/Python/python-lessons/the-door-in-the-back-of-the-classroom/Lesson_02/handling_exception_supplements/from_demo.py", line 13, in custom_sum
    raise SumError from e
SumError
```

Here what's happening is the line `sum += int(num)` causes a `ValueError` which is caught by our except block. We're then raising a totally different error to say that the sum function broke, but we raise it _from_ the `ValueError`. This places the `ValueError` as `.__cause__` of the `SumError`, which is why the line separating the two exceptions now reads `The above exception was the direct cause of the following exception:` instead.

This kind of error handling is best used in more complicated systems. Say for example that you've got a function to put some data in a database. This function will return a custom `PutDataError` if the data isn't placed in the database. Now, just a `PutDataError` is going to be a bit naff, you'll not gleam much info from that. So instead we catch various other exceptions and place the blame on those.  
Let's look at some sample code:

```python
class PutDataError(Exception):
    """An exception raised by the put_data method upon failure"""


def put_record(data):
    """Places record in table, if record already exists an exception is
    raised as you should use the update function.

    Database schema:

    `id`: uuid4, `name`: str, `phone_no`: str & '\+\d{12}'

    Not all fields required, but all fields must conform to expected
    datatype."""

    exp = PutDataError(F"Failed to put data: {data}")

    try:
        validate_data(data)
    except InvalidDataError as e:
        raise exp from e

    try:
        session = start_database_session()
    except ClientError as e:
        raise exp from e

    try:
        response = put_data(session, data)
    except DatabaseError as e:
        raise exp from e

    print(F"{response=}")
```
So you can see here, we'll always send out a `PutDataError` if things fail, but upon inspection you will be able to gleam the underlying issue as it will be named the "direct cause" of the `PutDataError`. This makes catching exceptions raised out of our `put_record` really simple and easy whilst not making it difficult to pin-point the precise issue   

This code is available to mess around with [here](./handling_exception_supplements/database_example.py). It imports code from [here](./handling_exception_supplements/database.py). At this point in our lessons you should be able to understand it all except for maybe the `global` keyword and the RegEx stuff.
