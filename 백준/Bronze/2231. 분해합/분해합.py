N = int(input())
result = 0

for i in range(1,N):
    total = i
    temp = i
    while temp > 0:
        total += temp % 10
        temp //= 10
    if total == N:
        result = i
        break
print(result)