import itertools
letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 4]
names = ['james', 'nicole']
combined = itertools.chain(letters, numbers, names)
for i in combined:
    print(i)