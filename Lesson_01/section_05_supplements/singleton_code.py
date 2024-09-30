

class MySingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, something):
        self.something = something


if __name__ == "__main__":
    singleton_1 = MySingleton(something=3)
    singleton_2 = MySingleton(something=99)

    print(F"{singleton_1.something}")
    print(F"{singleton_2.something}")

    singleton_1.something = 'something else'

    print(F"{singleton_1.something}")
    print(F"{singleton_2.something}")
