class Greet:
    def __init__(self, greeting):
        self.greeting = greeting
    def __call__(self, name):
        return self.greeting + ' ' + name
print(id(Greet.__call__))
Greet.__call__ = lambda self, name: self.greeting + ' ' + name + '!'
print(id(Greet.__call__))
greeter = Greet('Hello')
print(greeter('World'))