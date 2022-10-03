def all_equal(array):
    is_all_equal = True
    for i in array:
        for j in array:
            if i != j:
                is_all_equal = False
                break
    return is_all_equal

print(all_equal([1, 1, 1]))
