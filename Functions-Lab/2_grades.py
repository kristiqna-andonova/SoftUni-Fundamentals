grade = float(input())


def solve(grades):
    if 2.00 <= grades <= 2.99:
        return "Fail"
    elif 3.00 <= grades <= 3.49:
        return "Poor"
    elif 3.50 <= grades <= 4.49:
        return "Good"
    elif 4.50 <= grades <= 5.49:
        return "Very Good"
    elif 5.50 <= grades <= 6.00:
        return "Excellent"


print(solve(grade))

