import itertools
numbers = [0, 1, 2, 3]
result = itertools.product(numbers, repeat=3)
for i in result:
    print(i)