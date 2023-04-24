string = [float(x) for x in input().split()]
numbers = []


def rounding_fun(num):
    result = [round(number) for number in num]
    return result


print(rounding_fun(string))
