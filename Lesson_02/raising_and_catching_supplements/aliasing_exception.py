

if __name__ == "__main__":
    some_dict = {
        'a': 'apple',
        'bee': 'buzz',
        'c': 'carrot',
    }

    for key in ['a', 'b', 'c']:
        try:
            print(F"{key} is for {some_dict[key]}")
        except Exception as e:
            print("EXCEPTION!")
            print(e)
