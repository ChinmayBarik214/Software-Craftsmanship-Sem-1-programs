def modifyList(my_list):
    my_list.append(3)
    return my_list
print('List')

old_list = [1, 2]
print(id(old_list))

new_list = modifyList(old_list)
print(id(new_list))

def modifyNumber(number):
    number += 5
    return number
print('Integer')
old_number = 5
print(id(old_number))

new_number = modifyNumber(old_number)
print(id(new_number))