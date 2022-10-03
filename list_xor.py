def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    for i in list1:
        if i == n and n in list2:
            return False
    return True

print(list_xor(1, [0, 0, 0], [4, 5, 6]) )
