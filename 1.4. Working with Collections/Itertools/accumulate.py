import itertools
numbers = [1, 2, 3, 2, 1, 0]
result = itertools.accumulate(numbers, lambda x, y: x*y)
for item in result:
    print(item)