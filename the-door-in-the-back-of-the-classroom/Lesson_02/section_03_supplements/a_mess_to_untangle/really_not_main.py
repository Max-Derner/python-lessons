

def foo(a):
    for i in range(100):
        _ = a[i]


def bar(b):
    a = str(b) * 99
    foo(a)
