number = int(input())

for num in range(1, number + 1):
    sum_of_digits = 0
    digits_as_str = str(num)

    for i in digits_as_str:
        sum_of_digits += int(i)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

