numbers_as_str = input().split()
numbers = []

for num in numbers_as_str:
    number = float(num)
    numbers.append(abs(number))

print(numbers)
