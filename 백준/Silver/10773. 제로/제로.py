import sys
input = sys.stdin.readline

K = int(input().strip())
stack = []
for _ in range(K):
    x = int(input().strip())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))