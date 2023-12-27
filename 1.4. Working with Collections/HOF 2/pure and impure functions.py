# impure function
def append_4(input_list):
    input_list.append(4)
    return input_list
# pure function
def append_4(input_list):
    temp_list = input_list[:]
    temp_list.append(4)
    return temp_list