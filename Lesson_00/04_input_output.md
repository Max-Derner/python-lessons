```
 ___ ___  
|_ _/ _ \ 
 | | | | |
 | | |_| |
|___\___/ 
```
# CLI
## Output
You've got `print()` which gets the job done. There is a logging library for proper applications but we'll get to that in another lesson.  
You have `\n` for line breaks if you want them but `print` automatically adds a line break at the end.
You can put what you like into print and it'll still print:  
``` python
print("Hello World!")
print(my_int)
print(print)  # See how you can pass the function into itself? Functions are "1st class citizens" in Python!
```
Don't want the line break at the end?
Do this:
``` python
print("All on...", end='')  # end='' prevents the line break
print("one line!")
```
Need to put data into a string? There is something called an [f-string](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)
```python
my_data = 3
print(f"There is {my_data} data")  # the 'f' can be upper or lower case
```
F-strings (or "formatted string literals") are super duper cool, there's a tonne you can do with them for terse code that produces clean and expressive output. There are also many ways to format strings in Python, beyond the f-string most take on a style similar C or Bash.  
Please get a look at [the docs](https://docs.python.org/3/tutorial/inputoutput.html) if you want to dive a little deeper.

My favourite uses of f-strings are these format specifiers (there was a [link to them](https://docs.python.org/3/library/string.html#formatspec) on that last page I sent you to):
```python
Python 3.14.7 (main, Aug  5 2026, 10:29:49) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> my_num = 1.123456789
>>> print(f"Look at this: {my_num:.2f} init cool!?")  # the ':.2f' gives you 2 decimal places
Look at this: 1.12 init cool!?
>>> print(f"What about this? {my_num=}")  # the '=' gives you a neat formatting to show what you are inspecting as well as the value
What about this? my_num=1.123456789
>>> print(f"{(my_num ** 3) % 5=}")  # for example, you can use it to show the result of full expressions
(my_num ** 3) % 5=1.4179767796223608
>>> print(f"{' MIDDLE ':=^80}")  # you can even pass string literals in there
==================================== MIDDLE ====================================
>>> 

```
## Input
You've got `input()`.  
Assign the return value of input to a variable, and pass in the user prompt. This return value will **_always_** be a `str`ing.  
``` python
user_input = input("Enter something: ")
```
That will show up on the CLI as:
```
Enter something: _
```
Where the underscore is the cursor (i.e. it's always inline with the prompt unless you start passing line breaks).

# File
We've got the function `open()` but it should always be used in what's called a "context manager" (we'll do a deep dive on context managers in a later lesson).  
So say you're reading a file called `text.txt`, you do it like this:
``` python
with open("text.txt", mode='r') as f:  # here f represents the file io stream
    # use 4 spaces of indentation to define the scope
    the_whole_file_as_a_string = f.read()
```

So long as we keep 4 spaces of indentation to define the scope (known as a codeblock), we can use the file io stream 'f'. Once we exit the codeblock we can't use `f` anymore as the file will be closed. When using a context manager files will always automatically close (even if an error is thrown or you try to exit the interpreter altogether).


Now, say you want to write to a file, you use the same context manager but you give it a different mode:
``` python
with open("text.txt", mode='w') as f:  # mode is 'w' for write
    f.write("Some text or something I guess")
```
There's only one method to write, so make sure to include your line breaks if you want them.

| **WARNING** |
|-------------|
| `mode='w'` will overwrite the whole file, if you only want to add to the file, use `mode='a'` for "append" |

# STDIN

Yeah! You can totally read from STDIN, this lets you pipe text right into your file if you did the whole shebang and make it executable thing.

```python
from sys import stdin

line = stdin.readline()
```

## Quick note about reading text
Both the `f` object returned by the `open` function, and `stdin` both inherit from [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase). So there's actually a tonne of cross over.

## That's it here, [let's get going](./05_operations.md)