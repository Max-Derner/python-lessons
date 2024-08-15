```
  ___                       _   _                 
 / _ \ _ __   ___ _ __ __ _| |_(_) ___  _ __  ___ 
| | | | '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \/ __|
| |_| | |_) |  __/ | | (_| | |_| | (_) | | | \__ \
 \___/| .__/ \___|_|  \__,_|\__|_|\___/|_| |_|___/
      |_| 
```

# School Maths
So let's review the regular mathematical operations:
``` python
a = 22
b = 7
c = a + b
d = a - b
e = a * b
f = a / b  # division always returns a float
g = a ** b  # this is a to the power of b, some languages have it as a ^ b
```
Note that every operator is separated with spaces.

# Quirky Maths
You've got your extra bits in python too:
``` python
c = 22 // 7  # this is floor division, c will evaluate to 3
d = 22 % 7  # this is the modulo operator (what's the remainder after division), d will evaluate to 1 
```

# Terse Maths

In Python, you're ok to reassign like this:
``` python
e = e / f
```
And that applies to any of the operators we just saw.

You can also do a cooler shorthand, with any of the operators we've seen so far:
``` python
e /= f
```
So, right there our equals has been replaced with an equals and an operator smushed together, and that applies for any of the operators we've seen. These two expressions are equal.

_NOTE:_ We don't have increment and decrement operators, so you can't do a++, ++a, --a, or a--.



# Boolean Operations
Let's not get too bogged down here...  
Most of it is obvious but you'll still need to see the syntax:
``` python
thing or other_thing
thing and other_thing
not thing
```
So we don't have `!` or `&&` or `||` or `&` or `|`, we just use the English words `not`, `or`, and `and`.   

Example:
``` python
True or False  # evaluates as True
True and False  # evaluates as False
not False  # evaluates as True
```

# Equality

Broadly speaking, you use double equals, like this:
``` python
some_list == []  # this evaluates to True if "some_list" is am empty list
```
There are occasions where you should use the keyword `is` instead of `==`. This is when you want to assert that they are the same object.  
In Python, there is one `True`, one `False`, and one `None`. So if you're testing for equality to one of those values, you need to use the `is` keyword. So you'll end up with expressions like:  
``` python
something is True
something_else is None
```

# None Equality
For values, it's:
``` python
thing_1 != thing_2
```

For checking it's not the exact same object, like when you [copy a list wrong (check the "_**SECOND QUICK NOTE:**_")](./02_variables.md#collections) go for:  
``` python
my_copy is not your_copy
```

### [Onwards and upwards!](./06_logic_gates.md)