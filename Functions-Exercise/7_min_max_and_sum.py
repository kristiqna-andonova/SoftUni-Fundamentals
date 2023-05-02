numbers = [int(x) for x in input().split(" ")]


def min_number(lists):
    return f"The minimum number is {min(lists)}"


def max_number(lists):
    return f"The maximum number is {max(lists)}"


def sum_number(lists):
    return f"The sum is: {sum(lists)}"


print(min_number(numbers))
print(max_number(numbers))
print(sum_number(numbers))