def greet(name):
    return 'Hello ' + name
print(greet('World'))
new_greet = greet
print(new_greet('World'))