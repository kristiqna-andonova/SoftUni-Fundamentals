first_list = input().split(", ")
second_list = input().split(", ")

search_word_list = []

for word in second_list:
    for searched_word in first_list:
        if searched_word in word:
            search_word_list.append(searched_word)
            break
print(sorted(set(search_word_list)))
