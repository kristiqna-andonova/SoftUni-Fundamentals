number_type = str(input())
number = input()


def data_type_teller(inputs, num):
    result = 0
    if inputs == "int":
        n = int(num)
        result = n * 2

    elif inputs == "real":
        n = float(num)
        result = f"{n * 1.5:.2f}"

    elif inputs == "string":
        string = str(num)
        return f"${string}$"

    return result


print(data_type_teller(number_type, number))
