numbers_str = input().split()
numbers = []

for num in numbers_str:
    number = float(num)
    numbers.append(abs(number))

print(numbers)
