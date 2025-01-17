```
 ____       _               
/ ___|  ___| |_ _   _ _ __  
\___ \ / _ \ __| | | | '_ \ 
 ___) |  __/ |_| |_| | |_) |
|____/ \___|\__|\__,_| .__/ 
                     |_| 
```

# Installing Python
Good news! It's probably already installed!
Run the following command in your CLI:
``` bash
python3 --version
```
If you get back something like `Python 3.12.4` then you're all set.

If not, give one of these a go:
* [Windows](./Install_Instructions/Windows.md)
* [Mac](./Install_Instructions/Mac.md)
* [WSL (Ubuntu)](./Install_Instructions/WSL.md)

**N.B.** For learning, just install the latest version available. If you're on a project, bloody well use what they tell you to use!!

# Setting up an IDE
Don't you **_dare_** use IDLE, it's the "IDE" that bundled with Python but it's worse than worse, just don't subject yourself to it.

Pick VSCode or PyCharm.  
* PyCharm hits the ground running but holds your hand to the point of getting clammy and it recently had a [security vulnerability which threatened to expose all of your GitHub access tokens](https://blog.jetbrains.com/security/2024/06/updates-for-security-issue-affecting-intellij-based-ides-2023-1-and-github-plugin/).
* VSCode just needs the `Python`, and `Flake8` extensions installing and you're good to go (**I prefer VSCode**)

**N.B.** Just for this lesson, don't worry about how much flake8 tells you off. I don't want you to worry about errors like "`blank line contains whitespace`", "`too many blank lines`", "`line too long (93 > 79 characters)`", or "`no newline at end of file`".  
This is all readability stuff and does not impact how the code runs. We'll go over it together in a future lesson but if you want to look it up yourself it all comes under the [PEP8 standards](https://peps.python.org/pep-0008/).

# Setting up a venv
So real quick, a venv is a `v`irtual `env`ironment. It isolates your Python version and installed libraries from other projects and more importantly - your base Python installation. If you install libraries against your base Python version, other projects will need to account for having that library installed when they install dependencies, this will break a lot of stuff.  

To create a venv called "my-cool-venv" (assuming you have Python installed now), you run:
``` bash
python3 -m venv my-cool-venv
```
To activate the "my-cool-venv" venv, you run:
``` bash
source ./my-cool-venv/bin/activate
```
....unless you're on bloody Windows!!  
Then you have to run:
```
my-cool-venv\Scripts\activate
```
If you are on Windows, I totally recommend using WSL by the way. It puts a little Linux right inside your machine which is just beautiful <3

# Installing 3rd party libraries
Pick one from PyPI [here](https://pypi.org/), let's say you picked `pandas`.  
With your venv active, run:
``` bash
pip install pandas
```
or whatever library you're installing. Again, we'll add professionalism to this later.


| WARNING |
|---------|
| Make sure you **ONLY** ever install libraries onto a venv. Installing libraries without use of a venv will absolutely knacker your setup. But we'll talk more next lesson

# Using libraries
Beyond what you install on your venv, there's [an absolute tonne of included libraries](https://docs.python.org/3/library/index.html#library-index). Check out [my favorites for newcomers](./maxs_fav_libs.md)  
To import (and then use) a library, say `json`, you'd do this:
``` python
import json
my_json_string = json.dumps(some_python_dictionary)
```
Imports can be done anywhere in your code, but traditionally they're done at the top of the file.  

## Importing libraries well
So, you never ever import multiple libraries on one line like this:
```python
import json, pprint
```
This makes broken libraries and modules a pain to get figured out. So you do this:
```python
import json
import pprint
```
You can also alias a library if you get sick of writing out the full name every time:
```python
import json as js
js.dumps(some_python_dictionary)
```
If you don't want all of a library, you can import just little bits of it. So, instead of this:
```python
import time
print("Hold on...")
time.sleep(1)
print("The epoch time is:")
print(time.time())
```
You can do this:
```python
from time import time, sleep
print("Hold on...")
sleep(1)
print("The epoch time is:")
print(time())
```
In this situation, we're only importing one module on the one line so it's allowed, but you can break that import across multiple lines if you like:
```python
from time import (
    time,
    sleep,
)
print("Hold on...")
sleep(1)
print("The epoch time is:")
print(time())
```
You can even alias the individual items you're importing from that module/library:
```python
from time import (
    time,
    sleep as zzz,
)
print("Hold on...")
zzz(1)
print("The epoch time is:")
print(time())
```

# Actually running some code
Just slap some code in a `.py` file (e.g. `my_code.py`) and then pass the filepath into the `python3` command.  
e.g. `python3 my_code.py`  

If you've got your venv active then you can just give the command `python my_code.py` without specifying python**3**  
Don't worry too much about whether you're doing it right for this lesson, as long as you get some code running that's what matters. I just want you playing around and getting to grips with the basics today, we'll bring professionalism into it later.

### Extra bit of usefulness...
You can type code in directly against the interpreter in the REPL (Read Evaluate Print Loop). To do so, just type `python3` (or simply `python` with a venv active).  
This can be a little tricky as it doesn't really have code-completion or suggestions.  
**N.B.** To exit the interpreter give it the command `exit()` (as keyboard interrupts won't work)  
The interpreter will print out anything returned by an expression or function, as well as what is supposed to be printed to the console.

## One last word...
There are many many ways to set up your Python environment. I only suggest the above as what I consider to be that with the fewest headaches. But please do take a look around at what else is on offer, you may very commonly hear of [PyEnv](https://github.com/pyenv/pyenv), [Poetry](https://python-poetry.org/docs/), and [Anaconda](https://www.anaconda.com/).

If you are only just getting started in Python, forget about those... then remember them much much later and look into them then.

# What else?
Nothing. That's all you're getting at this point, we're just keen to get a thin base going to build on top of.  
### [Let's move on](./02_variables.md)
