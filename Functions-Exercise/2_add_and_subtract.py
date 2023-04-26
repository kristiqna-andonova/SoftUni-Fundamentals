first_number = int(input())
second_number = int(input())
third_number = int(input())


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


sum_result = add(first_number, second_number)
result = subtract(sum_result, third_number)

print(result)
