

def dodgy_function(key) -> str:
    """Uses `key` to access a dictionary

    Problems:
    * presumes that the key is hashable
    * presumes key exists in dictionary
    * throws exception for specific key types"""

    if isinstance(key, set):
        2 / 0
    dodgy_dict = {
        'sea': 'wet',
        'dirt': 'dirty',
        'cat': 'meow',
    }
    return dodgy_dict[key]
