```
 ____       _     _             
|  _ \ __ _(_)___(_)_ __   __ _ 
| |_) / _` | / __| | '_ \ / _` |
|  _ < (_| | \__ \ | | | | (_| |
|_| \_\__,_|_|___/_|_| |_|\__, |
                          |___/ 
 _____                    _   _                   _____                    
| ____|_  _____ ___ _ __ | |_(_) ___  _ __  ___  |  ___| __ ___  _ __ ___  
|  _| \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \/ __| | |_ | '__/ _ \| '_ ` _ \ 
| |___ >  < (_|  __/ |_) | |_| | (_) | | | \__ \ |  _|| | | (_) | | | | | |
|_____/_/\_\___\___| .__/ \__|_|\___/|_| |_|___/ |_|  |_|  \___/|_| |_| |_|
                   |_|                                                     
 _____                    _   _                 
| ____|_  _____ ___ _ __ | |_(_) ___  _ __  ___ 
|  _| \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \/ __|
| |___ >  < (_|  __/ |_) | |_| | (_) | | | \__ \
|_____/_/\_\___\___| .__/ \__|_|\___/|_| |_|___/
```

# Why?

Well, there may be times where something goes wrong and you are trying to handle an exception but something goes even wronger! In this situation you _could_ raise a brand new exception on it's own, or you could raise a new exception that has the old one as context for what you were doing.

# What?
Let's look at what happens by default.  
Say you're doing something that raises an exception, you then try to handle it and something else goes wrong and raises an exception...

```python
try:
    'me'/2
except Exception as e:
    'you' ** 'python lessons'
```
What you get is a traceback like this:
```
Traceback (most recent call last):
  File "/home/max-derner/LnD/python-lessons/the-door-in-the-back-of-the-classroom/Lesson_02/section_05_supplements/double_raise.py", line 4, in <module>
    'me'/2
    ~~~~^~
TypeError: unsupported operand type(s) for /: 'str' and 'int'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/max-derner/LnD/python-lessons/the-door-in-the-back-of-the-classroom/Lesson_02/section_05_supplements/double_raise.py", line 6, in <module>
    'you' ** 'python lessons'
    ~~~~~~^^~~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
```
You essentially get the first exception printed out, a line reading "`During handling of the above exception, another exception occurred:`", and then the second exception. This lets you know what initially went wrong and then what went wrong while trying to handle that issue.


