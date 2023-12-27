numbers = [7, 91, 25, 43, 64, 37]
iterable = [ i % 2 == 0 for i in numbers]
if any(iterable):
    print('The given numbers has at least one even number')
else:
    print('The given numbers does not have an even number at all')