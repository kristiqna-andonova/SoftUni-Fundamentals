number = int(input())


def is_perfect(num):
    perfect_sum = 0
    for i in range(1, num):
        if num % i == 0:
            perfect_sum = perfect_sum + i
    if perfect_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(is_perfect(number))
