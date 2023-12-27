from functools import wraps
def add_exclamation(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) + '!'
    return wrapper
@add_exclamation
def greet(name):
    return 'Hi ' + name
print(greet('User'))