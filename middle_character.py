def mid(string):
    length = len(string)
    if length % 2 == 0:
        return ""
    return string[int(length / 2)]

print(mid("abc"))
