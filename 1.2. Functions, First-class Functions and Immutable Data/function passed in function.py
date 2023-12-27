def louder(word):
    return word.upper()
def whisper(word):
    return word.lower()
def greet(name, func):
    return 'Hello ' + func(name)
print(greet('World', louder))
print(greet('World', whisper))