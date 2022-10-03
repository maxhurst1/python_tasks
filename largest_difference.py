def largest_difference(array):
    largestNumber = -100
    smallestNumber = 100

    for number in array:
        if largestNumber < number:
            largestNumber = number
        if smallestNumber > number:
            smallestNumber = number
    return largestNumber - smallestNumber
    
print(largest_difference([1, 2, 3]))
