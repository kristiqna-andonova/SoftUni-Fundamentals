numbers_list = list(map(int, input().split(", ")))

event_list = []

for num in numbers_list:
    if num % 2 == 0:
        event_list.append(numbers_list.index(num))

print(event_list)
