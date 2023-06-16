first_number = int(input())
second_number = int(input())
third_number = int(input())


def is_positive_fun(a, b, c):
    if (a > 0 and b > 0 and c > 0)\
            or (c > 0 and a < 0 and b < 0)\
            or (b > 0 and a < 0 and c < 0)\
            or (a > 0 and b < 0 and c < 0):
        print("positive")

    elif a == 0 and b == 0 and c == 0:
        print("zero")

    else:
        print("negative")


is_positive_fun(first_number, second_number, third_number)
