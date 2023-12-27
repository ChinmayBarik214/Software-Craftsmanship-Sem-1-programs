import functools
class Calculator:
    def add(self, a, b):
        return a + b
    add_2 = functools.partialmethod(add, 2)
calc = Calculator()
print(calc.add_2(3))