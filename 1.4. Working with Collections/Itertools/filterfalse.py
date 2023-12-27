import itertools
List = ["a", "b", "C", "d"]
result = itertools.filterfalse(str.isupper, List)
for i in result:
    print(i)