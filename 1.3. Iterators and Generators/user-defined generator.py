def generator(low, high): # generates a counter
    while low <= high:
        yield low
        low += 1
for i in generator(5,10):
    print(i, end=' ')
print('\na')
a = generator(3, 4)
print(type(a)) # generator object not list object
print(next(a), end=' ')
print(next(a), end=' ')
print(next(a), end=' ')
