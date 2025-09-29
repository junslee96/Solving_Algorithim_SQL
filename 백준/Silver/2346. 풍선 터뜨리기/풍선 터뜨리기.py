from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
moves = list(map(int,input().split()))
dq = deque((i+1,moves[i]) for i in range(N)) #(풍선번호,이동값)
order = []

while dq:
    idx, k = dq.popleft()
    order.append(idx)
    if not dq:
        break
    if k > 0:
        dq.rotate(-(k-1))
    else:
        dq.rotate(-k)
print(*order)