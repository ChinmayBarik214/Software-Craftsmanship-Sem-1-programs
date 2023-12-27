def greet(a):
    return 'Hi ' + str(a)
numbers = [1, 2, 3, 4, 5]
mapped_numbers = map(greet, numbers)
print(list(mapped_numbers))