```
 _         _   _             __  __ _                                
| |    ___| |_( )___    ___ / _|/ _(_)_ __   __ _   _ __ _   _ _ __  
| |   / _ \ __|// __|  / _ \ |_| |_| | '_ \ / _` | | '__| | | | '_ \ 
| |__|  __/ |_  \__ \ |  __/  _|  _| | | | | (_| | | |  | |_| | | | |
|_____\___|\__| |___/  \___|_| |_| |_|_| |_|\__, | |_|   \__,_|_| |_|
                                            |___/                    
                          _   _     _             _ 
 ___  ___  _ __ ___   ___| |_| |__ (_)_ __   __ _| |
/ __|/ _ \| '_ ` _ \ / _ \ __| '_ \| | '_ \ / _` | |
\__ \ (_) | | | | | |  __/ |_| | | | | | | | (_| |_|
|___/\___/|_| |_| |_|\___|\__|_| |_|_|_| |_|\__, (_)
                                            |___/  
```
# What are we doing then?
Let's write a little guessing script!  
We'll set up a string and have the user guess the word or phrase. We'll need variables, input, output, loops, comparisons, and a main clause.

# Variable Naming Convention
You've got three styles of variable name but it's always "[snake case](https://en.wikipedia.org/wiki/Snake_case)".  
**Classic** (lower case): `my_variable`  
**Constant** (all caps): `DONT_CHANGE_ME` (this is also known as "screaming snake case")  
**Private** (prefix with underscore): `_dont_use_me_elsewhere`  

The funny thing about this is none of that is enforced by the interpreter, so it's _all_ scouts honour. You can change constants as much as you want, and use private variables and methods wherever you like, the interpreter don't care none.

# Creating and Running a Python Script
* Well, you need a Python file but that file can be any name so long as it has a `.py` extension. It's surprisingly uncommon to see a `main.py` so don't feel like you have to do that.  
* Now you can just bash some code into the file.  
* To run it depends on whether you have your venv active
    * If your venv is active just type `python <path-to-file>` and that's it! Congrats!
    * If your venv is not active, you'll need to specify which Python runtime you want to use. This can be as none-specific as `python3 <path-to-file>`, or as specific as `python3.11 <path-to-file>`

# Quick tip
With Python being an interpreted language it is possible to write code and have it executed at the same time, all you need to do is not specify a file when giving the `python3` or `python3.11` command. This will open up an interpreter directly in the console, now you can just type away. The interpreter catches _all_ errors which means you can't use keyboard interrupt to get out of the interpreter, instead you have to give the code `exit(0)`, the 0 is just the exit status.  
Now, using the interpreter like this is great if you can't remember how a particular thing works like list slicing, or dictionary merging, etc. But it gets tricky when you're experimenting with more than a few lines of code.

# Learn a little Python
* Strings are declared as `my_str = 'hi` or `my_str = "hello"`, there's no difference between using double or single quotes.  
* Output is done like `print("hello")` or `print(my_str)`, you can pass strings, numbers, variables or expressions and even functions directly, and print will always output even if it's not a string type (I mean, as long as your expression didn't break things).
    * If you want a new line, you can either issue an empty print statement ( `print()` ), or put a new line character in the string ( `\n` ).
* Input is done with `user_input = input("This is me telling you to input something: ")`, the result of input will always be a string.  
* String formatting can be done with `F"You entered: {user_input}"`, as long as you have a lower or uppercase 'f' before the first quote then you can use curly braces to drop numbers, variables, or expressions into a string (there are lots of ways to format strings but this is the the most readable).  
* You can check the length of most things (strings, lists, dictionaries, sets, etc) using the `len()` function. e.g. `len('hello')` will return 5.
* Comparisons can be done with:
    * | operator | plain english | notes |
      |----------|---------------|-------|
      | a == b | is 'a' equal to 'b' | this is comparison by value, not comparison by reference |
      | a != b | is 'a' not equal to 'b' | this is comparison by value, not comparison by reference |
      | a > b | is 'a' greater than 'b' | strings will compare with alphabetical order |
      | a < b | is 'a' less than 'b' | strings will compare with alphabetical order |
      | a >= b | is 'a' greater than or equal to 'b' | strings will compare with alphabetical order |
      | a <= b | is 'a' less than or equal to 'b' | strings will compare with alphabetical order |
* While loops:
    * ```# while loop
        while a == b:
            print("Still equal!)
        print("Stopped being equal!")
       ```
    * Be careful to note the four spaces of indentation, this is how you define scope in Python. Indented code is called a "code block", the `print("Still equal!)` can be referred to as the "while block".
    * Also note the lack of parenthesis, including them can get you in trouble but we'll save that story for later.
* If Else logic flow:
    * ```# if else
        if a > b:
            print("a is the best!")
        elif b > a:
            print("b is the best!")
        else:
            print("They both suck!")
        ```
    * Same comments as the while loop, 4 spaces of indentation, no parenthesis.
* Main clause:
    * ```# main clause
        print("I am code that will always run, regardless of if this file is executed as main. For example, when importing something from this Python file")
        if __name__ == "__main__":
            print("I will only execute if you run this file as main")
    * It's a bit kooky, but aren't all main clauses?
    * Note the indentation again. Like I said, it's the way we define scope in Python.

# Let's get a first script written then!
I don't want you to worry about errors like "`blank line contains whitespace`", "`too many blank lines`", "`line too long (93 > 79 characters)`", or "`no newline at end of file`".  
This is all readability stuff and does not impact how the code runs. We'll go over it together later on but if you want to look it up yourself it all comes under the [PEP8 standards](https://peps.python.org/pep-0008/).

## I trust you, you got this!
Well, you know what we're doing. Why don't I recap the ask and you can see if you can get it done?  
I want a script that prompts the user to guess a phrase (or word, or letter), the user should guess until they get it right.


## You want a little bit more hand-holding?
No worries, it's all new so I get that. Let me walk you through it step by step, I'll not show you any code yet though.

1. Start a main clause, making sure to pay attention to the indentation
1. Hard code a constant string variable to hold your secret phrase (or secret word, or secret letter for that matter)
1. Initialise an empty string to hold guesses
1. Start a while loop to check whether the guess matches your secret phrase (or word, or letter)
1. On an indented code block (at this point it should by 8 spaces from the margin), assign the result of `input()` to the guess variable
1. Use an if statement to check whether the guess is wrong.
1. If the guess is wrong, tell the user.
    * You can optionally tell them whether the length of their guess is right or not perhaps saying "guess too long" or "guess too short"
1. Now out the outside of the while block, tell the user that they guessed correctly!

## You don't want to do it first? You just want to see my code?
That's fair enough, I get it if you're busy and just want to get through stuff. I do recommend that you give it a try but totally respect your choice.

Go get a look at [first_code_example.py](./first_code_example.py)