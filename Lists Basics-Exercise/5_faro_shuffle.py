cards = input().split()
counter = int(input())

for _ in range(counter):
    first_half = []
    second_half = []

    for i in range(1, len(cards) - 1):
        card = cards[i]
        if i < len(cards) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    shuffled = []
    first_part_i = 0
    second_part_i = 0

    for i in range(len(first_half) * 2):
        if i % 2 == 0:
            shuffled.append(second_half[second_part_i])
            second_part_i += 1
        else:
            shuffled.append(first_half[first_part_i])
            first_part_i += 1

    cards = [cards[0]] + shuffled + [cards[-1]]

print(cards)
