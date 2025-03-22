```
  ____            _            _     __  __                                       
 / ___|___  _ __ | |_ _____  _| |_  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___ 
| |   / _ \| '_ \| __/ _ \ \/ / __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__/ __|
| |__| (_) | | | | ||  __/>  <| |_  | |  | | (_| | | | | (_| | (_| |  __/ |  \__ \
 \____\___/|_| |_|\__\___/_/\_\\__| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|  |___/
                                                              |___/
```
Last thing now and then we'll finish up for this lesson

You have seen a context manager already, they are a function or class that you interact with using the `with` keyword. You know them from file handling:
```python
with open("some_file.txt", mode='r') as file_stream:
    file_content = file_stream.read()
```
In this instance `open()` is your context manager.

# What and why?

Right, well context managers are here to DRY up use of `try/finally` statements. In the same way functions are here to prevent you writing the same piece of logic over and over again, context manages are here to prevent you writing the same piece of error handling over and over again.  
By this point you may have come to understand that Pythons exception handling is fairly rich and powerful (and not in the oligarch kinda way). This comes down to the way we use exceptions in Python. In Python you basically raise an exception anytime you fail to do something. This way if you ask a piece of code to do something and it can't, it will force you to face that fact and now you've got a choice; either cope by using an except block, or panic by letting it bubble up (maybe someone further up the line can handle it anyway). With this level of exception use, it stands to reason that you might have certain patterns emerging around exception handling. So, let's dream up an example of the `try/finally` pattern...

So, let's say we are programming some sort of robot that gathers environmental data and transmits that data back to base once every 8 weeks. If something were to go wrong with our code at any point, we'd want to a) transmit what data we do have and b) call someone to repair us. So, without the context manager that would look something like this:

```python
def main():
    initialise_data_channel()
    data_store = DataCollection()
    # For this example we'll bring the transmission period down to only
    # 5 seconds and set the program to gather data every 0.5 seconds.
    data_store.transmission_period = timedelta(seconds=5)
    collection_period = timedelta(seconds=0.5)
    last_data_collection = datetime.now()
    while True:
        current_time = datetime.now()
        time_since_last_collection = current_time - last_data_collection
        if time_since_last_collection >= collection_period:
            print("Collecting data")
            data = collect_data()
            last_data_collection += collection_period
            data_store.commit_record(data)
            print("collected")
        if data_store.data_due_to_send:
            print("Sending data...")
            transmit_data(data_store.format_for_transmission())
            data_store.reset()
            print("sent")
```

The [code is here](./context_managers_supplements/no_context_management.py), you can run the code and watch the data coming into a file called `data_transmission.txt`. Now to illustrate the issue, hit `ctrl + C` and observe your `data_transmission.txt` file. Notice anything missing? Well, the problem is that when you interrupted the program it didn't send the data it had been gathering since the last transmission, and that is true of any exception that might occur.

# The try finally pattern

The way you would have had to handle this prior to context managers is like this:
```python
def main():
    initialise_data_channel()
    data_store = DataCollection()
    # For this example we'll bring the transmission period down to only
    # 5 seconds and set the program to gather data every 0.5 seconds.
    data_store.transmission_period = timedelta(seconds=5)
    collection_period = timedelta(seconds=0.5)
    last_data_collection = datetime.now()
    try:
        while True:
            current_time = datetime.now()
            time_since_last_collection = current_time - last_data_collection
            if time_since_last_collection >= collection_period:
                print("Collecting data")
                data = collect_data()
                last_data_collection += collection_period
                data_store.commit_record(data)
                print("collected")
            if data_store.data_due_to_send:
                print("Sending data...")
                transmit_data(data_store.format_for_transmission())
                data_store.reset()
                print("sent")
    finally:
        print("An issue has arisen!")
        print("Conducting emergency transmission of remaining data...")
        transmit_data(data_store.format_for_transmission())
        print("sent")
```

Here you can see we try that entire loop, and if anything goes wrong we make sure our final action is send an emergency transmission of the remaining data.  
Try running that code (which can be [found here](./context_managers_supplements/try_finally_pattern.py)), interrupt it, and check your output data. Unless your data was already due for transmission or had just been transmitted, you should see an unusually short chunk of data in the last transmission and the terminal will have output that it is sending said emergency transmission. 

# The class based context manager
I like the class based context managers, I just find them friendlier than their function based counterparts.  
To make a context manager class, you simply have to declare a class that has an `__enter__` method and an `__exit__` method. The `__enter__` method is called when we start the `with` block, it can return things to be aliased using the `as` keyword. The `__exit__` method has to accept 3 arguments defining the exception type, the exception itself and the exceptions traceback, and if it returns `True` then the exception will be suppressed, `False` and the exception will bubble up. You may also optionally declare an `__init__` method which can be used to initialise the context manager.

So, an example will clear that up.

```python
class MyContextManager:

    def __init__(
            self,
            transmission_period: timedelta = timedelta(weeks=8),
    ):
        self.data_store = DataCollection()
        self.data_store.transmission_period = transmission_period

    def __enter__(self) -> DataCollection:
        initialise_data_channel()
        return self.data_store

    def __exit__(self, exc_type, exc_value, traceback):
        # you may inspect these values 'exc_type', 'exc_value', and
        # 'traceback' to determine the error and whether an error has
        # happened to suppress and whether to reraise the exception
        if exc_type is not None:
            print(F"An issue has arisen! {exc_type}")
            print("Conducting emergency transmission of remaining data...")
        else:
            print("Sending remaining data...")
        transmit_data(self.data_store.format_for_transmission())
        print("sent")
        # return a boolean to indicate whether or not you are
        # suppressing the exception
        return True if exc_type == KeyboardInterrupt else False


def main():
    last_data_collection = datetime.now()
    collection_period = timedelta(seconds=0.5)
    with MyContextManager(
        transmission_period=timedelta(seconds=5),
    ) as data_store:
        while True:
            current_time = datetime.now()
            time_since_last_collection = current_time - last_data_collection
            if time_since_last_collection >= collection_period:
                print("Collecting data")
                data = collect_data()
                last_data_collection += collection_period
                data_store.commit_record(data)
                print("collected")
            if data_store.data_due_to_send:
                print("Sending data")
                transmit_data(data_store.format_for_transmission())
                data_store.reset()
                print("sent")
    
    # You will only see this if the context manager
    # suppresses the exception
    print("a graceful end")
```

So here you can see that we have created a custom class. This class defines three dunder methods `__init__()`, `__enter__()`, and `__exit__()`. The `__init__()` method is still what's used to initialise the context manager, you can see that happening in the `main()` function where it goes:
```python
with MyContextManager(
    transmission_period=timedelta(seconds=5),
)
```
Then the `__enter__()` method is what defines the context managers behaviour when it's called using the `with` statement. We have decided to return something from our `__enter__()` method which can then be used in the `with` block if you assign it to a variable using the `as` keyword which we saw in the `main()` function where it goes `as data_store`:
```python
        ...
        transmission_period=timedelta(seconds=5),
    ) as data_store:
```
Then the `__exit__()` method is what defines the error handling. This method does whatever you would normally do in the finally block plus deciding which exceptions to suppress. In our method we've decided to suppress any `KeyboardInterrupt` exceptions but anything else will bubble up and halt the system.  
For clarity, suppressing an exception with your context manager still means the code exits the context manager. Ideally the way you would use this feature is that whatever you return from the `__enter__` method would have a custom exception that gets caught by the `__exit__` method, this way we're saying that "If the context manager itself runs into a problem, then we can shut it down gracefully".


Hopefully, you can see why I quite like the class based context manager. You have 3 separate methods which all have very clear and distinct roles, and there is no need anything too complex. Let's compare this to the function based context manager.


# The function based context manager

Now, we've already seen what a context manager does so this bit will be easier and shorter. However, there is a new keyword we'll be seeing here which we're yet to cover. I'll make sure to exactly mimic the behaviour of our class based context manager so you can more easily see the difference.

So with the function based context manager, you need to import `contextmanager` from `contextlib` and use it as a decorator. You also need to use a try finally pattern yourself to provide the same behaviour.

```python
@contextmanager
def my_context_manager(transmission_period: timedelta = timedelta(weeks=8)):
    # initialisation here
    data_store = DataCollection()
    data_store.transmission_period = transmission_period
    # __enter__ style code here
    initialise_data_channel()
    try:
        yield data_store
    # __exit__ style code here
    except KeyboardInterrupt as e:
        print(F"An issue has arisen! {type(e)}")
        print("Conducting emergency transmission of remaining data...")
    except Exception as e:
        print(F"An issue has arisen! {type(e)}")
        print("Conducting emergency transmission of remaining data...")
        raise
    else:
        print("Sending remaining data...")
    finally:
        transmit_data(data_store.format_for_transmission())
        print("sent")
```

So what was in the `__init__` method before is now just the first few lines of the function:
```python
def my_context_manager(transmission_period: timedelta = timedelta(weeks=8)):
    # initialisation here
    data_store = DataCollection()
    data_store.transmission_period = transmission_period
```

Next up is the code that begins the error handling and provides whatever resource you wish to use. Providing that resource is done via the `yield` keyword, we're not going to worry about that keyword for now but I'll get to it in the next lesson.
```python
    # __enter__ style code here
    initialise_data_channel()
    try:
        yield data_store
```

Now we need to define the behaviour of our error handling which can be a bit awkward really in the sense that we can no longer just check a couple of variables, we need to use all the tricks in the error handling bag. This makes it quite difficult for newcomers to the language and even some of the more seasoned developers may not be aware of all these tricks.

```python
    # __exit__ style code here
    except KeyboardInterrupt as e:
        print(F"An issue has arisen! {type(e)}")
        print("Conducting emergency transmission of remaining data...")
    except Exception as e:
        print(F"An issue has arisen! {type(e)}")
        print("Conducting emergency transmission of remaining data...")
        raise
    else:
        print("Sending remaining data...")
    finally:
        transmit_data(data_store.format_for_transmission())
        print("sent")
```


