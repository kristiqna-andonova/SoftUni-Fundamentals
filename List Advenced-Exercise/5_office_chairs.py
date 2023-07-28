lines = int(input())

free_chairs = 0
is_free = True

for room in range(1, lines + 1):
    current_num = input().split()
    chairs = len(current_num[0])
    visitors = int(current_num[1])

    if chairs - visitors >= 0:
        free_chairs += abs(visitors - chairs)
        is_free = True
    else:
        is_free = False
        print(f"{abs(chairs - visitors)} more chairs needed in room {room}")

if is_free:
    print(f"Game On, {abs(free_chairs)} free chairs left")
