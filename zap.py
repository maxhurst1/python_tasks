def zap(a, b):
    zapped_list = []
    for i in range(len(a)):
        zapped_list.append((a[i], b[i]))
    return zapped_list

print(zap([0, 1, 2, 3], [5, 6, 7, 8]))
