numbers = int(input())
word = input()

strings = []
strings_including_word = []

for _ in range(numbers):
    current_word = input()
    strings.append(current_word)

    if word in current_word:
        strings_including_word.append(current_word)

print(strings)
print(strings_including_word)
