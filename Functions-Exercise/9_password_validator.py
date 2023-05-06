password = input()


def lent_checker(passwords):
    return 6 <= len(passwords) <= 10


def letters_and_number_checker(passwords):
    return passwords.isalnum()


def digits_counter(passwords):
    digits_count = 0
    for ch in passwords:
        if ch.isdigit():
            digits_count += 1
    return digits_count >= 2


is_valid = True

if not lent_checker(password):
    is_valid = False
    print("Password must be between 6 and 10 characters")

if not letters_and_number_checker(password):
    is_valid = False
    print("Password must consist only of letters and digits")

if not digits_counter(password):
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")
