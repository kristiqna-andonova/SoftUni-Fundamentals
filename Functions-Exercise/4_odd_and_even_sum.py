number_str = input()


def odd_or_even_sum(inputs):
    odd_sum = 0
    even_sum = 0

    for num in inputs:
        number = int(num)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(odd_or_even_sum(number_str))
