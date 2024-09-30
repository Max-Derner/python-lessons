

class GettingAndSettingClass:

    def __init__(self, initial_value: int):
        self.my_var = initial_value

    @property
    def my_var(self):
        return self._my_var

    @my_var.setter
    def my_var(self, value):
        # isinstance() is a built-in function: https://docs.python.org/3/library/functions.html#isinstance
        if isinstance(value, int) and value >= 0:
            self._my_var = value
        else:
            print(
                "Negative value or incorrect type provided for 'my_var'"
                ", setting to 0"
            )
            self._my_var = 0


if __name__ == "__main__":
    initial_value = -1
    acceptable_value = 12345
    incorrect_type = "HELP!!!"
    print(F"Supplying initial value: {initial_value=}")
    a = GettingAndSettingClass(initial_value)
    print(F"{a.my_var=}")
    print(F"Supplying acceptable value: {acceptable_value=}")
    a.my_var = acceptable_value
    print(F"{a.my_var=}")
    print(F"Supplying incorrect type: {incorrect_type=}")
    a.my_var = incorrect_type
    print(F"{a.my_var=}")
