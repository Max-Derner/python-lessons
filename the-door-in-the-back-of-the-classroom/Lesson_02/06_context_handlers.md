```
  ____            _            _     _   _                 _ _               
 / ___|___  _ __ | |_ _____  _| |_  | | | | __ _ _ __   __| | | ___ _ __ ___ 
| |   / _ \| '_ \| __/ _ \ \/ / __| | |_| |/ _` | '_ \ / _` | |/ _ \ '__/ __|
| |__| (_) | | | | ||  __/>  <| |_  |  _  | (_| | | | | (_| | |  __/ |  \__ \
 \____\___/|_| |_|\__\___/_/\_\\__| |_| |_|\__,_|_| |_|\__,_|_|\___|_|  |___/
```

# Last thing now and then we'll finish up for the day

You have seen context handlers already, they are a type of class that you interact with using the `with` keyword. You know them from file handling:
```python
with open("some_file.ext", mode='a') as file_stream:
    file_content = file_stream.read()
```
In this instance `open()` is a function which returns a context handler, which then returns itself... that was confusing. Let's get a feel for what a context handler does and then we can look at the anatomy of what the bloomin' heck I was just talking about.

# What do?
So, in simplest terms a context handler offers an interface for exception handling to the `with` keyword such that `with` can catch exceptions in it's code block and then hand them off to the context handler for handling. In terms of the `open()` function, it is actually returning a context handler which both handles exceptions and is 
