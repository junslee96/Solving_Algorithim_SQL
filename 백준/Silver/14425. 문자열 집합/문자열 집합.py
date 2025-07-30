import sys
input = sys.stdin.readline

N,M = map(int,input().split())
words = list(input().strip() for _ in range(N))
check = list(input().strip() for _ in range(M))
result = 0
for t in check:
    if t in words:
        result += 1
print(result)