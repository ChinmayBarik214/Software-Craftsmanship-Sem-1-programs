class Greet:
    def __init__(self, greeting):
        self.greeting = greeting
    def __call__(self, name):
        return self.greeting + ' ' + name
greeter = Greet('Hello')
print(greeter.greeting)
print(greeter('World'))