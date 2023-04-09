while True:
    lines = input()

    if lines == 'End':
        break

    if lines == 'SoftUni':
        continue

    for ch in lines:
        print(f"{ch}{ch}", end='')

    print()
