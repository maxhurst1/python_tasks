def is_anagram(string, anagram):
    contained_letters = list(string)
    same_letters = True
    for letter in anagram:
        if letter not in contained_letters:
            same_letters = False
    if same_letters and len(string) == len(anagram):
        return True
    return False

print(is_anagram("typhoon", "opython"))
