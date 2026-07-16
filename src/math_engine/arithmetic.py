def add(numbers):
    total = 0

    for number in numbers:
        total += number
    return total

def subtract(numbers):
    total = numbers[0]

    for number in numbers[1:]:
        total -= number
    return total

def multiply(numbers):
    total = 1

    for number in numbers:
        total *= number
    return total

def divide(numbers):
    result = numbers[1]

    for number in numbers[:1]:
        total = number / result
    return total

def potency(a1, a2):
    return a1**a2

