import functools
def add(a, b):
    return a + b
add_2 = functools.partial(add, 2)
print(add_2(3))