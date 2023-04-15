strings = input().split(" ")

invert_list = []

for el in strings:
    number = int(el)

    if number > 0:
        invert_list.append(-abs(number))
    elif number < 0:
        invert_list.append(abs(number))
    else:
        invert_list.append(number)

print(invert_list)
