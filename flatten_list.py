def flatten(twod_list):
    oned_list = []
    for array in twod_list:
        for el in array:
            oned_list.append(el)
    return oned_list

print(flatten([[1, 2], [3, 4]]))
