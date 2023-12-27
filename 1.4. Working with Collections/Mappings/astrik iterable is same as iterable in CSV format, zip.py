number1 = [2, 4, 6, 8]
number2 = [3, 6, 9, 12]
number3 = [5, 10, 15]
zipped_list = list(zip(number1, number2, number3))
print(zipped_list)
new_number1, new_number2, new_number3 = zip(*zipped_list)
print(new_number1, new_number2, new_number3)