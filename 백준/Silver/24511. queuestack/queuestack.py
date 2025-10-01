import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input().strip())
C = list(map(int,input().split()))

D = deque(b for a,b in zip(A,B) if a == 0)

out = []
for x in C:
    D.appendleft(x)
    out.append(str(D.pop()))
print(" ".join(out))