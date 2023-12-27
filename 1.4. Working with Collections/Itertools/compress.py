import itertools
letters = ['a', 'b', 'c', 'd']
selectors = [True, False, True, True]
result = itertools.compress(letters, selectors)
for i in result:
    print(i)