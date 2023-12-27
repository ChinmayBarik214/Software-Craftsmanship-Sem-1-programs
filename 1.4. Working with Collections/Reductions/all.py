numbers = [2, 4, 6, 8, 10]
iterable = [i % 2 == 0 for i in numbers]
if all(iterable):
    print('All the given numbers are even numbers')
else:
    print('All the given numbers are not even numbers')