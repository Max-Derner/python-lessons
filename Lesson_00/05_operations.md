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
```
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
```
c = 22 // 7  # this is floor division, c will evaluate to 3
d = 22 % 7  # this is the modulo operator (what's the remainder after division), d will evaluate to 1 
```

# Terse Maths

In Python, you're ok to reassign like this:
```
e = e / f
```
And that applies to any of the operators we just saw.

You can also do a cooler shorthand, with any of the operators we've seen so far:
```
e /= f
```
So, right there our equals has been replaced with an equals and an operator smushed together, and that applies for any of the operators we've seen. These two expressions are equal.

_NOTE:_ We don't have increment and decrement operators, so you can't do a++, ++a, --a, or a--.

# String Operations
## substring in string
To check if a string contains a substring you do it with the following expression:
```
substring in string
```
Example:
```
substring = "Hell"
string = "Hello World!"
substring_is_in_string = substring in string
```
The variable `substring_is_in_string` is now a `bool` with the value `True`.

Want to check a substring isn't in the string?
```
substring = "Heaven"
string = "Hello World!"
substring_is_not_in_string = substring not in string  # notice we just changed "in" for "not in"
```
Nice and simple
## concatenation
To smush two strings together, you simply add them like so:
```
part_a = "Hell"
part_b = "o World!"
complete = part_a + part_b
```
The variable `complete` now has a value of `Hello World!`.

This also applies to the `+=` operator:
```
iteratively_built_string = ''
iteratively_built_string += "Hell"
iteratively_built_string += "o World!"
```
The variable `iteratively_built_string` now has a value of `Hello World!`.  
You don't have to initially declare it as an empty string, I just like to because it makes later changing the order easier as git blame won't get confused.

# Logical Operations
Let's not get too bogged down here...  
Most of it is obvious but you'll still need to see the syntax:
```
thing or other_thing
thing and other_thing
not thing
```
So we don't have `!` or `&&` or `||` or `&` or `|`, we just use the English words `not`, `or`, and `and`. There are bitwise operators but that's something for another time.  

Example:
```
fave_char = 'b'
string_1 = 'abc'
string_2 = 'xyz'

fave_char in string_1 or fave_char in string_2  # evaluates as True
fave_char in string_1 and fave_char in string_2  # evaluates as False
fave_char in string_1 and fave_char not in string_2  # evaluates as True

```

# Equality

Broadly speaking, you use double equals, like this:
```
some_list == []  # this evaluates to True if "some_list" is empty
```
There are occasions where you should use the keyword `is` instead of `==`. This is when you want to assert that they are the same object.  
In Python, there is one `True`, one `False`, and one `None`.  
So if you're testing for equality to one of these values, you need to use the `is` keyword. So you'll end up with expressions like:  
```
something is True
something_else is None
```

# None Equality
For values, it's:
```
thing_1 != thing_2
```

For checking it's exact same object, like when you [copy a list wrong (check the "second quick note")](./02_variables.md#collections) go for:  
```
my_copy is not your_copy
```

### [Onwards and upwards!](./06_logic_gates.md)