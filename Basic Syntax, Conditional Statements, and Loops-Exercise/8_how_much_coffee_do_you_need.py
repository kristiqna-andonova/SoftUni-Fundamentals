coffee_count = 0

while True:
    line = input()

    if line == 'END':
        break

    if line == 'coding' or line == 'dog' or line == 'cat' or line == 'movie':
        coffee_count += 1
    elif line == 'CODING' or line == 'DOG' or line == 'CAT' or line == 'MOVIE':
        coffee_count += 2

print(coffee_count)
