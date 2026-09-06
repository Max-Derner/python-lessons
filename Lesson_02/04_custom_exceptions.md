```
  ____          _                  
 / ___|   _ ___| |_ ___  _ __ ___  
| |  | | | / __| __/ _ \| '_ ` _ \ 
| |__| |_| \__ \ || (_) | | | | | |
 \____\__,_|___/\__\___/|_| |_| |_|
                                   
 _____                    _   _                 
| ____|_  _____ ___ _ __ | |_(_) ___  _ __  ___ 
|  _| \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \/ __|
| |___ >  < (_|  __/ |_) | |_| | (_) | | | \__ \
|_____/_/\_\___\___| .__/ \__|_|\___/|_| |_|___/
                   |_|      
```

# Simple create
Creating custom exceptions is easy-peasy. All exceptions are just objects, so you simply need to create a new class and inherit from the correct place.

You will typically just do it like this:
```python
class MyCustomError(Exception):
    pass
```
`MyCustomError` has just inherited everything from `Exception` so you now treat it the same way you would any other exception. Do note that the class name doesn't end in `Exception` but instead ends in `Error`, this is traditional in Python and is just keeping up with all the other exceptions you're likely to see.

A slightly nicer way of doing this though is to explain where you should expect this new exception to be raised in a docstring! like so:  
```python
class MyCustomError(Exception):
    """A custom exception which is raised when thromdiculating the
    eldenburge fails"""
```


# A well structured family

You can actually inherit from any exception you like, so you could - for example - subclass the `ValueError` exception. If you wanted to you could create a whole family of exceptions of your own. Like this 3 generations of [retro-encabulator](https://www.youtube.com/watch?v=RXJKdh1KZ0w) exceptions.

```python
class RetroEncabulatorError(Exception):
    """Retro Encabulator failure"""


class UnilateralPhaseDetractorError(RetroEncabulatorError):
    """Failure to unilaterally detract the phase"""


class CardinalGrammeterSyncError(RetroEncabulatorError):
    """Failure to synchronise the cardinal gram meters"""


class ModialInteractionError(RetroEncabulatorError):
    """Modial interaction failed"""


class MagnetoReluctanceError(ModialInteractionError):
    """Magneto not reluctant"""


class CapacitiveDirectance(ModialInteractionError):
    """Capacitive indirectance occured"""
```


Well that was easy...

### [Let's look at what a context manager is](./05_context_managers.md)