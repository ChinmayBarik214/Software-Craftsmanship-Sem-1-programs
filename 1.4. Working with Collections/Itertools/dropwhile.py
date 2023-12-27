import itertools
numbers = [0, 1, 2, 3, 2, 1, 0]
def lt_2(n):
    if n < 2:
        return True
    return False
result = itertools.dropwhile(lt_2, numbers)
for item in result:
    print(item)