operator = input()
first_num = int(input())
second_num = int(input())


def calculator(operators, num_1, num_2):
    if operators == "multiply":
        return num_1 * num_2

    elif operators == "divide":
        return num_1 // num_2

    elif operators == "add":
        return num_1 + num_2

    elif operators == "subtract":
        return num_1 - num_2


result = calculator(operator, first_num, second_num)
print(result)
