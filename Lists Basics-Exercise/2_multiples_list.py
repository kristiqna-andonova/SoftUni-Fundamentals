factor = int(input())
count = int(input())

multiples = []

for num in range(1, count + 1):
    result = num * factor
    multiples.append(result)

print(multiples)
