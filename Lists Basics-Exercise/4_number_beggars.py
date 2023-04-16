numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for i in range(len(numbers)):
    beggars_i = i % beggars_count
    num = int(numbers[i])
    beggars[beggars_i] += num

print(beggars)
