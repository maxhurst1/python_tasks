def validate(code):
    if "def keyword" not in code:
        return "missing def"
    elif ":" not in code:
        return "missing :"
    elif ("(" in code or ")" in code) and "()" in code:
        return "missing paren"
    elif "    " not in code:
        return "missing indent"
    elif "validate" not in code:
        return "wrong name"
    elif "return" not in code:
        return "missing return"
    return True

print(validate("def keyword:( )    validate return"))
