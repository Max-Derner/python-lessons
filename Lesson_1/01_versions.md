```
__     __            _                 
\ \   / /__ _ __ ___(_) ___  _ __  ___ 
 \ \ / / _ \ '__/ __| |/ _ \| '_ \/ __|
  \ V /  __/ |  \__ \ | (_) | | | \__ \
   \_/ \___|_|  |___/_|\___/|_| |_|___/
```

# Semantics
First off, Python does **not** follow semantic versioning. Semantic versioning would mean that the only breaking changes occur across major versions, this is not the case with Python. In Python, breaking changes can happen across minor version increments (i.e. something that runs on the 3.8 runtime might break when you try to run it on the 3.9 runtime). Patch versions are wholly compatible, as they only contain security fixes (i.e. code running on the 3.8.3 runtime, is entirely compatible with the 3.8.9 runtime, and vice versa).

Python 3.8 was the last Python runtime to not be released on a yearly schedule, now we get a new minor release every year just in time for Christmas. Each minor release is then supported for 5 years.  
As I write this Python 3.8 is about to lose support this October, take a look at what is supported during what periods [here](https://devguide.python.org/versions/).

## What does supported mean?
While a Python runtime is "supported" this means it is actively getting security fixes released in incrementing patch versions. This means that if you wish to run a Python project for more than 5 years, you **_will_** have to upgrade minor versions at some point (or leave your code vulnerable to security exploits) so it's best to have a plan **_before_** you start any major projects.

# How will I know what breaks between versions?
[The python official docs](https://docs.python.org/3/contents.html) show exactly what is changing between versions. There are only a few places you really need to pay attention:
* **Removed** -> This is every feature being removed in this version. You'll not be able to use them and trying to will break everything
* **Deprecated** -> Don't fret about this, it's just all the bits that will get removed in a following version. You should address these as soon as possible but it won't stop your code from running.
* **Porting to Python 3.XX** -> This is advice based on the "Removed" and "Deprecated" sections

# What's my big impact?
Broadly, as a developer, you've only got one thing to really worry about. Is your Python version pre 3.10 or not?  
Python 3.10 brought with it a lot of changes. While you are learning Python I fully recommend installing 3.10 or better. As we progress through the lessons I will point out if something is pre or post 3.10 and you will gain an appreciation for the scope of change this runtime gave.

## [Next Section](./02_getting-set_up.md)








