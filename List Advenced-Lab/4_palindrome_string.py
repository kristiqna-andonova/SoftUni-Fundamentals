words = input().split()
key_word = input()

palindrome_list = []

for word in words:
    if word == word[::-1]:
        palindrome_list.append(word)

print(f"{palindrome_list}")
print(f"Found palindrome {palindrome_list.count(key_word)} times")
