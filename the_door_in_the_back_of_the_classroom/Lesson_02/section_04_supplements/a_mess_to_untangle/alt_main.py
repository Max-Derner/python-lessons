from not_main import baz

from traceback import print_exception


if __name__ == "__main__":
    for item in ['hey', 'hi', 'a', 'aayo!']:
        print(item)
        try:
            baz(item)
        except Exception as e:
            print_exception(e)
