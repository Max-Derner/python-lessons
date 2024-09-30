

# mutable default
def add_to_list(value, list_to_add_to: list = []):
    list_to_add_to.append(value)
    return list_to_add_to


# immutable default
def add_to_number(value, number_to_add_to: int = 0):
    number_to_add_to += value
    return number_to_add_to


# immutable default
def add_to_list_v2(value, list_to_add_to: list | None = None):
    if list_to_add_to is None:
        list_to_add_to = []
    list_to_add_to.append(value)
    return list_to_add_to


if __name__ == "__main__":
    print(F"{add_to_list(value=1)=}")
    print(F"{add_to_list(value=1)=}")
    print(F"{add_to_list(value=1)=}")

    print(F"{add_to_number(value=2)=}")
    print(F"{add_to_number(value=2)=}")
    print(F"{add_to_number(value=2)=}")

    print(F"{add_to_list_v2(value=3)=}")
    print(F"{add_to_list_v2(value=3)=}")
    print(F"{add_to_list_v2(value=3)=}")
