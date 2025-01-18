from typing import Any


def get_value_bad(dictionary: dict, key: Any) -> Any:
    """a pointless function since you can just access the dictionary
    yourself (See Lesson_00 - 02_variables for a variety of methods)"""
    try:
        return dictionary[key]
    except Exception as e:
        print(F"Whooops! Exception caught: {e}")
        return None


def get_value_good(dictionary: dict, key: Any) -> Any:
    """a pointless function since you can just access the dictionary
    yourself (See Lesson_00 - 02_variables for a variety of methods)"""
    try:
        return dictionary[key]
    except Exception as e:
        print(F"Whooops! Exception caught: {repr(e)}")
        return None


if __name__ == "__main__":
    my_dict = {'a': 'ayyy!', 'b': 'buzzzz', 'c': 'me now!'}
    print("Getting value with 'get_value_bad()'")
    value = get_value_bad(my_dict, 'd')
    print("Getting value with 'get_value_good()'")
    value = get_value_good(my_dict, 'd')
