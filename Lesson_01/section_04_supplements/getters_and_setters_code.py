

class GettingAndSettingClass:
    _my_var: int

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
            print("Negative value provided for 'my_var', setting to 0")
            self._my_var = 0
