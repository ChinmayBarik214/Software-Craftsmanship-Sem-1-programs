class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self # You’re now officially an iterator
    def __next__(self): # and now you can be iterated on with the for x in syntax
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
        return self.current - 1

print('\na')
a = Counter(5, 10)
for i in a:
    print(i, end=' ')
print('\nb')
b = Counter(3, 4)
print(next(b), end=' ')
print(next(b), end=' ')
print(next(b), end=' ')