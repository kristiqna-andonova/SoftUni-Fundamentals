lost_fights = int(input())
helmet_prise = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_count = 0
sword_count = 0
shield_count = 0
armor_count = 0

total_price = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        helmets_count += 1

    if fight % 3 == 0:
        sword_count += 1

    if fight % 6 == 0:
        shield_count += 1

    if fight % 12 == 0:
        armor_count += 1

total_price = \
    helmet_prise * helmets_count + \
    sword_price * sword_count + \
    shield_price * shield_count + \
    armor_price * armor_count

print(f"Gladiator expenses: {total_price} aureus")
