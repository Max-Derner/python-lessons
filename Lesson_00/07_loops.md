```
 _                          
| |    ___   ___  _ __  ___ 
| |   / _ \ / _ \| '_ \/ __|
| |__| (_) | (_) | |_) \__ \
|_____\___/ \___/| .__/|___/
                 |_|  
```

# For loop
You declare a for loop with:
```
for item in iterable:
    # do something with item
```
Note that 4 spaces of indentation define what code is in scope for the list

So, for example if you want to do a countdown, you could do this:
```
my_list = [5, 4, 3, 2, 1, 'blast off!']
for statement in my_list:
    print(statement)
```

If you don't want to define a list (which is a totally fair and normal thing to want), we use `range` like this:
```
for i in range(100):
    # do something with i
```
`range` can be used in a few different ways:
```
for i in range(100):
    # i begins at 0 and ends at 99

for i in range(5, 10):
    # i begins at 5 and ends at 9

for i in range(0, 10, 2):
    # i starts at 0 and ends at 9, BUT it takes steps of 2
    # so we only get even numbers and never actually see 9
```

Now, for loops are often used to do something x number of times but you don't actually care about the value of i.  
In Python, it is expected that you sort of throw i away and don't declare it.  
Do it like this:
```
for _ in range(20):
    # do something 20 times
```
The underscore can be used wherever you like to signify that you don't care about the return value.

# While loop
We don't have do-while loops, so don't ask.  You also define scope with 4 space of indentation here too  
Our while loops go:
```
while condition:
    # do a thing
```
So, we covered conditions in the latter part of the "operations" section.  
You can have:
```
While True:
    # infinite loop
```
Or:
```
user_input = ''  # remember truthy values in the variables section?
while not user_input:
    user_input = input("We really need some input, just give us anything please: ")
```
Or:
```
my_list = [1, 2, 3, 4, 5]
while my_list != []:
    print(my_list[0])
    del my_list[0]
```
Which will loop until the list has been consumed.


### Let's move onto the [last bit](./08_functions.md)
