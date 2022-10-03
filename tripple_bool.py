def triple_bool(bool1, bool2, bool3):
    for bo in [bool1, bool2, bool3]:
        if bo != True:
            return False
    return True

print(triple_bool(True, True, True))
