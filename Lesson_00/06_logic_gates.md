```
 _             _                    _            
| | ___   __ _(_) ___    __ _  __ _| |_ ___  ___ 
| |/ _ \ / _` | |/ __|  / _` |/ _` | __/ _ \/ __|
| | (_) | (_| | | (__  | (_| | (_| | ||  __/\__ \
|_|\___/ \__, |_|\___|  \__, |\__,_|\__\___||___/
         |___/          |___/    
```

Okie doke, the one thing you can rely on is if-else statements.  

# if elif else

Nice and simple, everyone knows them.  
Here's the syntax:
```
if expression1:
    # do something
elif expression2:
    # do something else
else:
    # do a different thing
```
The expressions are anything that can be evaluated as "truthy/falsy".  
Notice that we're using the 4 spaces of indentation to define scope.  
Also notice that we don't use curly braces (`{}`) to define scope, that's done with an indented codeblock like it is everywhere else in Python.

Example:
```
if some_number % 2 == 0:
    print("That's an even number!")
elif some_number % 2 == 1:
    print("That's an odd number!")
else:
    Print("That was a fraction!")
```

# match-case
So, if you have Python3.10 or newer, you will be able to use match-case statements. Though you will likely know them as switch statements.  
They are just about my favourite thing in Python and they go like this:
```
match object:
    case pattern1:
        # do something
    case paettern2:
        # do something else
    case _:
        # do some default behaviour
```
**N.B.** `case _:` marks the default cae, **also** notice that you do not have to break between cases

There's more to match-case statements but we'll swing round to that in a different lesson

### Off to the [next adventure!](./07_loops.md)