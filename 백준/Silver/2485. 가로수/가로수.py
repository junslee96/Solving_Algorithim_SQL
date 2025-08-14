import sys
input = sys.stdin.readline

def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

N = int(input().strip())
pos = [int(input().strip()) for _ in range(N)]
diffs = [pos[i+1]-pos[i] for i in range(N-1)]

g = diffs[0]
for d in diffs[1:]:
    g = gcd(g,d)

answer = (pos[-1] - pos[0]) // g - (N-1)
print(answer)