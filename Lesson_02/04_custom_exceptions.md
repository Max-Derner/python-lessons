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

Well that was easy...

### [Let's look at what a context manager is](./05_context_managers.md)