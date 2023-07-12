names_list = input().split(", ")

sorted_name_list = sorted(names_list, key=lambda x: (-len(x), x))

print(sorted_name_list)