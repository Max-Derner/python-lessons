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

Somethign about the from keyword e.g.

```python
try:
    'me'/2
except Exception as e:
    try:
        # something else
    except Exception as exp:
        raise exp from e
```