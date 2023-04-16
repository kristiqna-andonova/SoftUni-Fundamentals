string = [int(x) for x in input().split(" ")]
counter = int(input())

for _ in range(counter):
    string.remove(min(string))

for i in range(len(string)):
    num = string[i]
    if i == len(string) - 1:
        print(num)
    else:
        print(num, end=", ")
