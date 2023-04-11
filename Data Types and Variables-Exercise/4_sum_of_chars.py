lines = int(input())

result = 0
for _ in range(lines):
    ch = input()
    result += ord(ch)

print(f"The sum equals: {result}")
