import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)