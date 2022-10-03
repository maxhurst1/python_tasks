def format_number(number):
    backwards_number = list(str(number))
    formatted_number = ""
    index = 0

    for num in reversed(backwards_number):
        if index == 3:
            formatted_number += ","
            index = 0

        formatted_number += num
        index += 1
    return formatted_number[::-1]

print(format_number(123456789))
