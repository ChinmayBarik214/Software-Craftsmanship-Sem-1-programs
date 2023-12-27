def add(a):
    def add_a(b):
        return a + b
    return add_a
print(add(2)(3))