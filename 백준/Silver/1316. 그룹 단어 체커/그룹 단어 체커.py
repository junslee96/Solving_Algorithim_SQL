N = int(input())
words = [input() for _ in range(N)]
count = 0
for word in words:
    seen = set()
    last_char = ''
    for char in word:
        if char != last_char:
            if char in seen:
                break
            seen.add(char)
            last_char = char
    else:
        count += 1
print(count)