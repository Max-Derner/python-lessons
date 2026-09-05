from time import sleep


class Demo:
    an_int = 1
    a_list = ['a']

    def __init__(self, name: str):
        self.name = name


def print_all(*args: Demo):
    print()
    input("Press enter to reveal values...")
    justification = 20
    for obj in args:
        output = ''
        output += f"name: '{obj.name}'".ljust(justification)
        output += f"| an_int: {obj.an_int}".ljust(justification)
        output += f"| a_list: {obj.a_list}".ljust(justification)
        print(output)
    input("Press enter to continue...")
    print()


if __name__ == "__main__":
    print("Instantiating object 'a'")
    a = Demo('a')
    print_all(a)

    print("=== Modifying variables with respect to class ===")
    print("an_int + 99 & a-list + 'b'")
    Demo.an_int += 99
    Demo.a_list.append('b')
    sleep(2)

    print()
    print("Instantiating object 'b'")
    b = Demo('b')
    print_all(a, b)

    print("Instantiating object 'c'")
    c = Demo('c')
    print_all(a, b, c)

    print("=== Modifying variables with respect to instance 'a' ===")
    print("an_int + 72 & a-list + 'c'")
    a.an_int += 72
    a.a_list.append('c')
    sleep(2)

    print_all(a, b, c)

    print("=== Reassigning variables with respect to instance 'a' ===")
    print("an_int = 42 & a-list = ['hay', 'bee', 'sea']")
    a.an_int = 42
    a.a_list = ['hay', 'bee', 'sea']
    sleep(2)

    print_all(a, b, c)

    print("=== Reassigning variables with respect to class ===")
    print("an_int = 60 & a-list = ['w', 'h', 'a', 't', '?']")
    Demo.an_int = 60
    Demo.a_list = ['w', 'h', 'a', 't', '?']
    sleep(2)

    print_all(a, b, c)
