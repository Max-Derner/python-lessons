```
  ____      _   _   _               ____       _     _   _       
 / ___| ___| |_| |_(_)_ __   __ _  / ___|  ___| |_  | | | |_ __  
| |  _ / _ \ __| __| | '_ \ / _` | \___ \ / _ \ __| | | | | '_ \ 
| |_| |  __/ |_| |_| | | | | (_| |  ___) |  __/ |_  | |_| | |_) |
 \____|\___|\__|\__|_|_| |_|\__, | |____/ \___|\__|  \___/| .__/ 
                            |___/                         |_|    
```

# Getting Set Up With a Version of Python

Nice and easy this one. It's probably already installed.  
Give this command to your CLI:
```
python3 --version
```
You're likely to get back something along the lines of `Python 3.12.2`. If you do, then you're set to get started.

## What if I want something really specific?
Well that's fair, every project will be working to a specific version and you might not have that installed yet.  
The subject of Python runtime management is a hotly debated subject amongst really boring people. My personal recommendation is to just install everything side by side using your traditional package manager. If you are on Linux, then you can add the "deadsnakes" repository to your package manager and take it from there.

## OS specific Instructions
Honestly, I trust you to be able to do this on your own but if you really want some advice...
* [WSL](./Install_Instructions/WSL.md)
* [Mac](./Install_Instructions/Mac.md)
* [Raw Windows](./Install_Instructions/Windows.md)
# Setting up an IDE
IDLE is the IDE that comes packaged with Python. It is the worst thing you have ever tried to use. Don't use IDLE.  
You want to use either PyCharm, or VSCode. 
* PyCharm hits the ground running but holds your hand to the point of getting clammy (recently had a [security vulnerability which threatened to expose all of your GitHub access tokens](https://blog.jetbrains.com/security/2024/06/updates-for-security-issue-affecting-intellij-based-ides-2023-1-and-github-plugin/)).
* VSCode just needs the `Python`, and `Flake8` extensions installing and you're good to go (I prefer VSCode)

# Virtual Environments
So, every Python project will need some 3rd party library installing at some point and _**you don't want to start installing 3rd party libraries to your base Python**_.  
Enter the "venv", or **V**irtual **ENV**ironment!  

A venv is a development environment that can be set up to use a specific version of Python, and in your venv you can install specific versions of libraries. So if you've got an AWS Lambda running with a particular Python runtime and it has installed particular libraries at particular versions, well you can replicate that environment in a venv.

To create a new venv:
1. Ensure you are in the root of the project directory
1. Choose a name for your venv and add it to the `.gitignore` (e.g. my-super-cool-venv)
1. Choose a runtime for your venv (or don't) but for example let's say we chose the 3.10 runtime
1. Issue into your CLI the command `python3.10 -m venv my-super-cool-venv` (if you didn't choose a runtime then replace `python3.10` with `python3`)

At this point there will be a new directory named after your venv, in that directory is a sub-directory called `bin/`, and in that sub-directory is (amongst other things) a number of "activate" scripts. These scripts activate your venv, allowing you to enter your new development environment and get started installing all those cool 3rd party libraries which can be found on [PyPI](https://pypi.org/) (the **Py**thon **P**ackage **I**ndex). If you're using Bash, just give the command `source my-super-cool-venv/bin/activate` to activate your venv. You can double check your venv is active by checking whether the environment variable `VIRTUAL_ENV` is populated, and if you want to exit your venv for any reason, then issue the command `deactivate`.


## Installing 3rd Party Libraries
This is another hotly debated topic amongst really boring people.  
"Pip" is the standard, but there are other package managers that claim to do a much better job such as "poetry", "pipenv", "conda", "pip-tools". I ain't going to talk about all that, let's just keep it simple, everyone who Pythons can Pip. If you join a Python project, then follow what they use but there ain't no sense in over-complicating matters if you've got something that works.

If you found a library on PyPI (let's say the [cryptography library](https://pypi.org/project/cryptography/)), then you will find the very simple instructions at the top of the page `pip install cryptography`. If you had your venv active at the time, then that library just got installed to your venv.  

## Surely there's a better way?
Now let's say you're working with others, you can't exactly supply people with a 100 libraries to manually install, can you?  
Enter "[the requirements file](https://pip.pypa.io/en/stable/reference/requirements-file-format/)"!

With the requirements file, you can create a `.txt` file with any name you like (though "**requirements.txt**" is traditional), and list every single requirement on a new line in that file. Now, say you called your requirements file requirements.txt then to install the requirements, you give the command `pip install -r requirements.txt`.

## What if I want a very particular version of a library?
You can [do that nice and easy](https://packaging.python.org/en/latest/specifications/version-specifiers/#id5). The basics of it are as follows:
| Desired Version | Requirements Syntax | Application |
|-----------------|---------------------|-------------|
| exactly 1.34.74 | `boto3==1.34.74` | Bit of a last resort this, it's better if you're able to keep up with security patches |
| want at least 1.34.74 but get most recent security patch | `boto3=~1.34.74`| Best practice really this, absolutely no surprises and you keep up with security patches |
| want 1.34 but don't care about security patch version | `boto3==1.34.*` | This is ok, but try the above first, only resort to this if you struggle with dependency resolution. The `*` is a wildcard, you can do `boto3==1.*.*` if you only care about the major version. |
| want something newer than 1.34.74 but don't care what the major, minor, or patch version actually is | `boto3>=1.34.74` | Almost certain to break something when you accidentally get a different major version to what you planned on |
| want something older than 1.34.74 but don't care what the major, minor, or patch version actually is | `boto3<=1.34.74` | Also almost certain to break something when you accidentally get a different major version to what you planned on |
| want something between 1.28.14 and 1.34.139 | `boto3>=1.28.14,<=1.34.74` | Handy if you're stuck between a known security exploit and a breaking change, just don't stay stuck on this for too long |

**N.B.** With the less than or equal and the greater than or equal, you can get less than and greater than by just removing the `=` but it's still a bad idea.

## What if I want 1 requirements file for production, and 1 for devs?
That's cool, requirements files can link between each other, you can also specify more than one requirements file at a time.  

Say, we have two requirements files "reqs1.txt" and "reqs2.txt". You can either:
* Have developers install both from CLI as `pip install -r reqs1.txt -r reqs2.txt`. This is fine, until you have half a dozen requirements files.
* Link from inside one of the files, you can add the line `-r reqs2.txt` to the file reqs1.txt, now your developers only have to give the command `pip install -r reqs1.txt` and that will link across.
* Create a whole new requirements file, let's call it "dev-reqs.txt". Now in that file put the line `-r reqs1.txt` and below that put the line `-r reqs2.txt`. Now you've not changed either file but evs can still issue a simple command: `pip install dev-reqs.txt`. This is super handy for splitting dev requirements, test requirements, prod requirements, different containers requirements, etc.

## So I split my requirements files but now I have the same library named in multiple requirements files and the versions keep diverging, this seems terrible!
Enter the "[constraints.txt](https://pip.pypa.io/en/stable/user_guide/#constraints-files)" file!  

Constraints files are the identical twin to requirements files. They look exactly the same, but do different things. A requirements file says "You **_will_** install these libraries at these versions!", whereas the constraints file takes a more laid back approach and says "I don't care what you install but if you chose to install one of these libraries, you **_will_** install the version I tell you to!". So now you can remove all the version specifiers from your bajillion requirements files, and just specify the versions in a constraints file.

Constraints files are traditionally called "constraints.txt" but they can go by any name you like, same as the requirements files. Say you have a constraints file called "cons.txt", you specify it's usage not with `-r cons.txt` but with `-c cons.txt`. As long as you remember it's a `-c` not a `-r`, then you can do the same as you did with requirements files, link them from requirements files, link requirements files from constraints files, specify then both in the CLI command, list requirements file and constraints file all within a new file, do what you like really.

# Couple of pip tricks to wrap up with
| Command | Secret |
|----|-----|
| `pip install --upgrade pip` | Updates pip to latest |
| `pip list` | Shows what you've got installed |
| `pip freeze` | Outputs what is installed in a format that can dropped into a requirements file, so someone can mirror your venv |
| `pip show <installed package>` | Tells you what version you've got, what it is, who authors it, what the license is, what extra libraries it needs, what libraries need it |

**N.B.** Dropping the result of `pip freeze` into a requirements file is the surest way to accidentally include things you don't directly use but were installed as prerequisites of other libraries you do directly use.

## [Next Section](./03_less_than_the_basics_aka_lets_just_effing_run_something.md)
