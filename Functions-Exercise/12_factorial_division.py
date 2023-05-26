import math

first_number = int(input())
second_number = int(input())


def get_factorial(a, b):
    one = math.factorial(a)
    two = math.factorial(b)
    return f"{one / two:.2f}"


print(get_factorial(first_number, second_number))
