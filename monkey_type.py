from random import randint
value = input("Enter a string for monkey to type: ")

def monkey_type(string):
    characters = list("1234567890abcdefqhijklmnopqrstuvwxyz ")
    response = ""
    attempts = 0
    while True:
        for i in range(len(string)):
            response += characters[randint(0, len(characters) - 1)]
        if response == string:
            break
        attempts += 1
        response = ""
    print("Took monkey", attempts, "attempts")

monkey_type(value)
