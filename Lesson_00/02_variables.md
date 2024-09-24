```
__     __         _       _     _           
\ \   / /_ _ _ __(_) __ _| |__ | | ___  ___ 
 \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
  \ V / (_| | |  | | (_| | |_) | |  __/\__ \
   \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
```
# Naming Variables
Variable names follow `snake_case`  
Constants are in `SCREAMING_SNAKE_CASE`  
Privates have a `_leading_underscore`  

| **WARNING** |
|-------------|
| The Python interpreter could not care less about what's private or constant and will glady let you import a private variable from wherever and change a constant. This naming convention is just for IDEs and devs, so the whole thing operates on scouts honour. |

# Quick Note on the Typing System
Python is dynamically typed and strongly typed. So, variables can change types willy-nilly (dynamic) but using an incompatible type will throw an error (strong).  
We don't have to declare types, but we can do type hinting though - again - the interpreter doesn't give a damn about type hints, they're just for IDEs and devs. We'll get to type hints later since they could be their own entire lesson.

# Booleans
You've got `bool`.  
Declare it by assigning either `True` or `False`:
``` python
my_bool = True
```

# No value
You've got `None`, in other languages you'll have seen `null` or `void`. It's what you get when there ain't nothing to give.  
Declare it by assigning `None`:
``` python
my_none_type = None
```

# Numbers

## Whole numbers
You've got `int`, no long, no short, no int32.  
Declare it by assigning a number without a decimal place:
``` python
my_int = 1
```
If you've got a real big number, you can use an underscore as a thousands separator.  
e.g.
``` python
my_big_int = 1_000_000
```
The upper bound of integers is limited by memory, they are theoretically unbound. So you don't have to worry about overflow issues here.  
Example:
```
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2**9000
1861919823602446870051646947443265806218680881620164150161309755333181392347475969737916885903925979688282376725245050928552019850699830936678289110574564545897808148390669479768088103164174862614314896361751492419355200744919106773071079582599147802839706215610874713577461171484389014531465527630202236883843662826326484204605969450292309212479576754101484210438029392847117393209646612418243468945316443055403112189769994194382253211069075682210324665380367163398351260390065146550963353638226230571087153090476005831034463871223599543367440127371321307935600294235235555686651194174520755709233252147269712646152398661272615394330256766919854213808655136454478279520538925315159120689449046824765276993871084725126289174642261134186532952389529497451225294280309592333118547431857834022107299493307642886550035108349812538868548204110949267007844894921304724439232280030484032946555862021618822463975371563390466476093942333021906014621095132521668771544547398222309222385454252810109269995041305909748903485123565191403462125774254093965366838199092942669763234497755795922782368415391408328615941087687168142703569478330639528167193433105543630476588701348505543567751790789117717660152741734303989082897740369036292716627460893145378475903236426283709902853825833522685221030263417298462852391838147572583018386475574242223720125609852369550108535609838296845885540331405153336504029657425852682616998765068978970510668576704757343969900471616618487531217423608126248306049345412199702325217046285213249285846153975313978242675003402962824121160875928608618335006217051712260195130737083017631349816669929159176667868417353866905513835554999462637481342721400975639504482716709384155856026263304270260886740810287158032302083388891446551907198669473320114371718138443660594911466234734942910722449045244457975320043694169261701681656148362205170532994281152576853709669767416127252738437485793910219846836498268031157261792859230067295449184914230926461991700842371010236588596679342492743911615365711320743215987995901101163306076544568626531198809370907612331483471833845958618077480217892890533116603350040147116218227928732817945323636422047507156427135297222275812678187736036773320854938458989641651199078792658709405149957007882875374868180442468709128120647047303125901843060904208622152998500617510802742432155144605848971282208131749602408191808406410632175265171306237793956570406435402345476628467209068729893134433124291187516075267594298323098487990166243403468912628117388443154921474663149036640983804471509564893426039130480070632369458141251485052936042164865777219873983089572387511794739572152294019631222145910901210840561445507713655658889336373566800391206925212386456974315749376
```
## Decimals
You've got `float`, no doubles, no float64.  
Declare it by assigning a number with a decimal place:
``` python
my_float = 1.0
```
Floats **are** limited by your system architecture, you'll get 32bit floats on a 32bit system etc. So please do feel free to worry about this one.

# Text
There's just `str`ings, there's no chars.  
Declare it by assigning something between quotes:
``` python
my_str = "Hello World!"
my_other_str = 'Hello Galaxy!'
# The following two can start and end on different lines
# and will include any line feeds you put in them
my_str_which_is_usually_reserved_for_doc_strings = """Hello Universe!"""
my_str_which_is_quite_uncommon = '''Hello Multiverse!'''
```
We'll see docstrings later in this lesson, so don't fret if you didn't understand that bit

| need | command | note |
|------|---------|------|
| access character at index | `my_str[index]` | cannot be used to change value |
| discern if substring in str | `substring in my_str` | returns either `True` or `False` **AND** substring can be any length including 0 or 1 |
| concatenate 2 strings | `str1 + str2` | returns new string |
| | `str1 += str2` | modifies `str1` |


# Containers
_**QUICK NOTE:**_ Any of the objects under this section (and strings as it happens) can have their length checked by passing them into the `len()` function.  
_**SECOND QUICK NOTE:**_ These objects can't be copied with `my_copy = your_copy`, it has to be `my_copy = your_copy.copy()` but this is only a shallow copy, deep copies will come in a later lesson.  


## Key-Value Pairs (`dict`)
We call them `dict`ionaries, you might call them dictionaries, hash-maps, hash-tables, or something like that.  
Declare it by assigning some comma separated key-value pairs between braces, a key must be separated from a value by a colon `:`.
``` python
my_dict = {'key': 'value', 'a': 1, 1: 'one'}  # filled
my_dict = {}  # empty
```
| need | command | note |
|------|---------|------|
| access value | `my_dict[key]` | throws error when key doesn't exist |
| | `my_dict.get(key)` | returns `None` if key doesn't exist **OR** if key does exist but value is `None` |
| change value **OR** assign new key-pair | `my_dict[key] = value`|
| merge dictionaries | `dict1 \| dict2` | returns new dict **AND** if key exists in both `dict`s then value from dict2 takes priority **N.B.** only available in Python3.9 or higher |
|| `{**dict1, **dict2}` | returns new dict **AND** same key priority as above **AND** available regardless of version |
|| `dict1.update(dict2)` | returns `None` just updates `dict1` **AND** same key priority as above **AND** available regardless of version |
| remove key-pair | `del my_dict[key]` | |
| list keys | `my_dict.keys()`| does not return actual `list` object but mostly acts the same |
| list values | `my_dict.values()`| does not return actual `list` object but mostly acts the same |
| discern if key in dict | `key in my_dict` | returns either `True` or `False` |

### Additional notes
Dictionaries don't have a fixed length, and can contain any mix of types for both keys and values.  
Keys must be unique and hashable, to check if something is hashable use a CLI interpreter to pop it into the `hash()` function (e.g. `hash('HASH ME!')` ) as unhashable types throw errors.  

## Value only, duplicates allowed (`list`)
There's only `list`, no arrays, no vectors.  
Declare it by assigning some comma separated values between square brackets:
``` python
my_list = [1, 2, 'c', 'd']  # filled
my_list = []  # empty
```
| need | command | note |
|------|---------|------|
| access index | `my_list[index]` | can be negatively indexed to access values from other end (i.e. `my_list[-1]` returns last value, `my_list[-2]` returns penultimate value, etc) |
| add to list | `my_list.append(value)` | |
| merge lists | `list1 + list2` | returns new list |
|| `[*list1, *list2]` | returns new list |
||`list1.extend(list2)` | modifies list1 |
| remove index | `del my_list[index]` ||
| remove value | `my_list.remove(value)` | Only removes first instance of value **AND** throws error if value not present |
| sort list | `my_list.sort()` | sorts in place |
| reverse list | `my_list.reverse()` | reverses in place |
| discern if value in list | `value in my_list` | returns either `True` or `False` |

### Additional notes
Lists don't have a fixed length, and can contain any mix of types.  


## Value only, no duplicates (`set`)
We call this a `set`.  
Declare it by assigning some comma separated values between braces:
``` python
my_set = {1, 2, 'c', 'd'}  # filled
my_set = set()  # empty, remember {} is empty dict
```
| need | command | note |
|------|---------|------|
| add value | `my_set.add(value)` | |
| remove value | `my_set.discard(value)` | doesn't throw error if value not present |
| discern if value in set | `value in my_set` | Returns either `True` or `False` |

### Additional notes
Sets don't have a fixed length, and can contain a mix of types (so long as they're hashable but we'll get to that later).  
Sets don't maintain order, so you can't access a specific element.  

# Truthy/Falsy
There are truthy/falsy values in Python. Everything is truthy unless it's; zero, None, False, or empty.  

There is a really cool thing you can do in Python with Truthy/Falsy assignment. You can chain variables with the `or` keyword and the first one to not be Falsy is what will be assigned.
e.g.
``` python
my_list = []
my_dict = {}
my_int = 42
my_float = 3.9

something_truthy = my_list or my_dict or my_int or my_float
```
`something_truthy` will take on the value of `42` as everything before it was Falsy.

# Declaring Types!
So this is another thing the interpreter doesn't care about. Declare it one way and assign it the other, interpreter don't mind. A well set up IDE will help you keep to the declared types but really this is for you and the other devs working on your code.  

You've already seen all the types because I formatted them as inline code to cement it in your brain before you got here.  
So it goes like this:
``` python
my_int: int = 42
my_list: list = [1, 2, 3, 4]
# so on and so forth
```
It just goes `name: type = value`  
If you want to declare the content of a container, you get:
``` python
my_list: list[str] = ['this', 'is', 'cool']
my_dict: dict[int, str] = {1: 'one', 2: 'two'}
# N.B. You can't do it this way in Python3.8 but that's deprecated in two months anyway (Oct 2024)
```

Say you want to state a variable can take one value **_or_** another, it depends on the runtime version.  
Pre 3.10:
``` python
from typing import Union

my_list = list[Union[int, str]] = [5, 4, 3, 2, 1, 'blast off!']
```

3.10 and beyond:
``` python
my_list = list[int | str] = [5, 4, 3, 2, 1, 'blast off!']
```


# That's it?
Yeah, for now.
### [Moving on!](./03_comments.md)

