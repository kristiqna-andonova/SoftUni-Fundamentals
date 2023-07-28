words = input().split(" ")
even_word = []

for word in words:
    word_len = len(word)
    if word_len % 2 == 0:
        even_word.append(word)

print("\n".join(even_word))
