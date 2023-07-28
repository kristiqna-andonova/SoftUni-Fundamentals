numbers = list(map(int, input().split(", ")))

even = []
odd = []
positive = []
negative = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)


print(f"Positive:", end=" ")
print(*positive, sep=", ")
print(f"Negative:", end=" ")
print(*negative, sep=", ")
print(f"Even:", end=" ")
print(*even, sep=", ")
print(f"Odd:", end=" ")
print(*odd, sep=", ")
