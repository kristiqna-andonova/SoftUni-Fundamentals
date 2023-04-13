lines = int(input())

positive_list = []
negative_list = []

for _ in range(lines):
    current_num = int(input())

    if current_num >= 0:
        positive_list.append(current_num)
    else:
        negative_list.append(current_num)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
