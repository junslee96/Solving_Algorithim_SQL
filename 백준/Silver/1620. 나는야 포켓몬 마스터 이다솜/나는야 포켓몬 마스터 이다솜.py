import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pocketmons = list(input().strip() for _ in range(N))
name_to_number = {name: idx for idx,name in enumerate(pocketmons,start = 1)}

for _ in range(M):
    q = input().strip()
    if q.isdigit():
        print(pocketmons[int(q)-1])
    else:
        print(name_to_number[q])