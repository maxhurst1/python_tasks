def palindrome(string):
    backwards_string = string[::-1]
    if backwards_string == string:
        return True
    return False

print(palindrome("bob"))
