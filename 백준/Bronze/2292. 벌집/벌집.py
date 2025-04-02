N = int(input())
count = 1
limit = 1

while N > limit:
    limit += 6 * count
    count += 1
print(count)