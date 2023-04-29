numbers = [int(x) for x in input().split(" ")]


def is_even(number):
    return number % 2 == 0


print(list(filter(is_even, numbers)))
