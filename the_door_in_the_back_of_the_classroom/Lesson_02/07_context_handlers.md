```
  ____            _            _     __  __                                       
 / ___|___  _ __ | |_ _____  _| |_  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___ 
| |   / _ \| '_ \| __/ _ \ \/ / __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__/ __|
| |__| (_) | | | | ||  __/>  <| |_  | |  | | (_| | | | | (_| | (_| |  __/ |  \__ \
 \____\___/|_| |_|\__\___/_/\_\\__| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|  |___/
                                                              |___/
Last thing now and then we'll finish up for this lesson
```

You have seen a context manager already, they are a function or class that you interact with using the `with` keyword. You know them from file handling:
```python
with open("some_file.ext", mode='a') as file_stream:
    file_content = file_stream.read()
```
In this instance `open()` is your context manager.

# What and why?

Right, well context managers are here to DRY up use of `try/finally` statements. In the same way functions are here to prevent you writing the same piece of logic over and over again, context manages are here to prevent you writing the same piece of error handling over and over again.  
By this point you may have come to understand that Pythons exception handling is fairly rich and powerful (and not in the oligarch kinda way). This comes down to the way we use exceptions in Python. In Python you basically raise an exception anytime you fail to do something. This way if you ask a piece of code to do something and it can't, it will force you to face that fact and now you've got a choice; either cope by using an except block, or panic by letting it bubble up (maybe someone further up the line can handle it anyway). With this level of exception use, it stands to reason that you might have certain patterns emerging around `try/finally` pairs. So, let's dream up the example...

So, let's say we are programming some sort of robot that gathers environmental data and transmits that data back to base once a month. If something were to go wrong with our code at any point, we'd want to a) transmit what data we do have and b) call someone to repair us. So, without the context manager that would look something like this:

<!-- Very much doubting whether this is a good example, I just don't want to do a copy of open() -->

