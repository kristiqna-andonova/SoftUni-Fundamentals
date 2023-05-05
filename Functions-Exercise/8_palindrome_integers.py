number = input().split(", ")


def is_palindrome(numbers):
    for n in numbers:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


is_palindrome(number)
