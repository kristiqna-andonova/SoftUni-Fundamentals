electrons = int(input())

total_el_in_shell = 0
shells = []

for shell in range(1, electrons + 1):
    el_in_shell = 2 * shell ** 2
    total_el_in_shell += el_in_shell

    if total_el_in_shell >= electrons:
        shells.append(total_el_in_shell - electrons)
        break

    elif el_in_shell <= electrons:
        shells.append(el_in_shell)

    else:
        break

print(shells)
