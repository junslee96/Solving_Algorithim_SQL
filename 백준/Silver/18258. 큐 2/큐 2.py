import sys
from collections import deque
input = sys.stdin.readline

q = deque() # 큐 구현에 특화된 자료구조
N = int(input())
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        q.append(int(order[1]))
    elif order[0] == 'pop':
        print(q.popleft() if q else -1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(0 if q else 1)
    elif order[0] == 'front':
        print(q[0] if q else -1)
    elif order[0] == 'back':
        print(q[-1] if q else -1)