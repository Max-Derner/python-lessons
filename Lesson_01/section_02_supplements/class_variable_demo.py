

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
        output += F"name: '{obj.name}'".ljust(justification)
        output += F"| an_int: {obj.an_int}".ljust(justification)
        output += F"| a_list: {obj.a_list}".ljust(justification)
        print(output)
    input("Press enter to continue...")
    print()


print("Instantiating object 'a' as an instance of class 'Demo'")
a = Demo('a')
print_all(a)

print("=== Changing variables with respect to class ===")
Demo.an_int += 99
Demo.a_list.append('b')

print()
print("Instantiating object 'b' as an instance of class 'Demo'")
b = Demo('b')
print_all(a, b)

print("Instantiating object 'c' as an instance of class 'Demo'")
c = Demo('c')
print_all(a, b, c)

print("=== Changing variables with respect to instance 'a' ===")
a.an_int += 72
a.a_list.append('c')

print_all(a, b, c)

print("=== Changing variables with respect to class ===")
Demo.an_int += 60
Demo.a_list.append('bee')

print_all(a, b, c)
