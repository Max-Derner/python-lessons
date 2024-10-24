```
 ____        _ _ _        _           
| __ ) _   _(_) | |_     (_)_ __  ___ 
|  _ \| | | | | | __|____| | '_ \/ __|
| |_) | |_| | | | ||_____| | | | \__ \
|____/ \__,_|_|_|\__|    |_|_| |_|___/
```

# Getting to know them

Firstly, we don't really call them errors round these parts they're called exceptions. Having said that most exceptions are called "_Something_ Error". So no one actually cares whether you call them errors or exceptions.

Python has a nice selection of built in exceptions which you can raise or catch (or cause) for just about any occasion.  
A full list of the built-in exceptions can be found [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).  

What you are most likely to encounter are:
| Exception | Cause |
|-----------|-------|
| KeyError | No such key in dictionary |
| IndexError | No such index in list (or other sequence) |
| TypeError | Wrong object type |
| ValueError | Correct object type but an inappropriate value |
| FileNotFoundError | Tried to read a non-existent file |
| KeyboardInterrupt | Hit `ctrl + c` |

# Origin

Almost all exceptions have a common ancestor the plain `Exception` class. The exceptions to this lineage being being system exiting exceptions and that comes down to the way in which you can catch them, which we'll get to in a bit.

You can both raise and catch the `Exception` but you should only catch it with great caution and you should never raise it.

[Next!](./02_raising_and_catching_exceptions.md)
