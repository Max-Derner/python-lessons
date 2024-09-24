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
``` python
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
``` python
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
``` python
match object:
    case pattern1:
        # do something
    case pattern2:
        # do something else
    case _:
        # do some default behaviour
```
**N.B.** `case _:` marks the default case, **also** notice that you do not have to break between cases

But there's more to match-case statements!

You can use match-case to match against not just the explicit content of an object but it's structure instead. Say you've got some api, you've used the `json` library to convert the received JSON into a Python dict and now you want to check the shape of the data. You could do something like this:
```python
incoming = {
    'query_string': 'some query OR something like that',
    'meta-data': {'some': 'dictionary'},
    'some other stuff': 'whatever'
}

match incoming:
    case {'query_string': query, 'meta-data': meta, **kwargs}:
        print(F"{query=}")
        print(F"{meta=}")
    case _:
        print("Ooops! Done biffed it!")
```
Note the fact that we're assigning variables to aspects of the predicted input object.  
That outputs the following:
```
query='some query OR something like that'
meta={'some': 'dictionary'}
```
and if `incoming` changes to:
```python
incoming = {
    'body': {
        'query_string': 'some query OR something like that',
        'meta-data': {'some': 'dictionary'},
        'some other stuff': 'whatever'
    }
}
```
we get the following output:
```
Ooops! Done biffed it!
```

Have a play around with it and see what you can do!

### Off to the [next adventure!](./07_loops.md)