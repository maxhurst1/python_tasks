def capital_indexes(string):
    indexes = []
    for i in range(len(string)):
        if string[i].isupper():
            indexes.append(i)
    return indexes

print(capital_indexes("hElLo"))
