numbers = input().split(", ")


def is_palindrome(number):
    for n in number:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


is_palindrome(numbers)
