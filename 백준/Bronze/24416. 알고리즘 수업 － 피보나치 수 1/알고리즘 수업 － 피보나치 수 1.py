import sys
input = sys.stdin.readline

n = int(input().strip())

f = [0] * (n+1)
f[1] = f[2] = 1
for i in range(3,n+1):
    f[i] = f[i-1] + f[i-2]

cnt1 = f[n]
cnt2 = n - 2
print(cnt1, cnt2)