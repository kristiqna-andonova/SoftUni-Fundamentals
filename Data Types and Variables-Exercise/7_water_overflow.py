lines = int(input())

liters_in_the_tank = 0
for _ in range(lines):
    current_litter = int(input())

    if current_litter + liters_in_the_tank > 255:
        print("Insufficient capacity!")
        continue

    else:
        liters_in_the_tank += current_litter

print(liters_in_the_tank)
