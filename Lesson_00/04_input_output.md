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
You have `\n` for line breaks if you want them but print automatically adds a line break at the end.
You can put what you like into print and it'll still print:  
```
print("Hello World!")
print(my_int)
print(print)  # See how you can pass the function into itself? Functions are "1st class citizens" in Python!
```
Don't want the line break at the end?
Do this:
```
print("All on...", end='')  # end='' prevents the line break
print("one line!)
```
## Input
You've got `input()`.  
Assign the return value of input to a variable, and pass in the user prompt. This return value will **_always_** be a `str`ing.  
```
user_input = input("Enter something: ")
```
That will show up on the CLI as:
```
Enter something: _
```
Where the underscore is the cursor (i.e. it's always inline with the prompt unless you start passing line breaks).

# File
We only have the one function `open()` but it should always be used in what's called a "context manager" which we'll do a deep dive on later.  
So say you're reading a file called `text.txt`, you do it like this:
```
with open("text.txt", mode='r') as f:  # here f represents the file io stream
    # use 4 spaces of indentation to define the scope
    the_whole_file_as_a_string = f.read()
```
Or like this:

```
with open("text.txt", mode='r') as f:  # here f represents the file io stream
    # use 4 spaces of indentation to define the scope
    each_line_as_a_separate_element_of_a_list = f.readlines()
```
So long as we keep 4 spaces of indentation, we can use the file io stream 'f'. Once we drop the level of indentation (the indented section is known a a "code block") we can't use f anymore as the file will be closed. When using a context manager files will always automatically close (even if an error is thrown or you try to exit the interpreter altogether).


Now, say you want to write to a file, you use the same context manager but you give it a different mode:
```
with open("text.txt", mode='w') as f:  # mode is 'w' for write
    f.write("Some text or something I guess")
```
There's only one method to write, so make sure to include your line breaks if you want them.

**N.B.** `mode='w'` will overwrite the whole file, if you only want to add to the file, use `mode='a'` for "append"

## That's it here, [let's get going](./05_operations.md)