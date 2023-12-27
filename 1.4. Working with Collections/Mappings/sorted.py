# case-insensitive sorting
strings = ['HiJ', 'kLm', 'Abc', 'mnO', 'eFg', 'Pqr']
sorted_strings = sorted(strings, key=str.lower, reverse=True)
print(sorted_strings)