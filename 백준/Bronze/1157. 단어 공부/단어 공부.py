word = input().lower()

char_frequency = {}
for char in word:
    if char.isalpha():
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

max_frequency = max(char_frequency.values())
most_frequent_chars = [char for char, freq in char_frequency.items() if freq == max_frequency]

if len(most_frequent_chars) > 1:
    print("?")
else:
    print(most_frequent_chars[0].upper())