words = [input() for _ in range(5)]
max_length = max(len(word) for word in words)
for i in range(max_length):
    for word in words:
        if i < len(word):
            print(word[i], end='')