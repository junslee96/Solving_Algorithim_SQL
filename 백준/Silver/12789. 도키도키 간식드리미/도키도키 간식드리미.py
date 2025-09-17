import sys
input = sys.stdin.readline

N = int(input())
tickets = list(map(int,input().split()))
stack = []
want = 1

for x in tickets:
    while stack and stack[-1] == want:
        stack.pop()
        want += 1
    if x == want:
        want += 1
    else:
        stack.append(x)
        
while stack and stack[-1] == want:
    stack.pop()
    want += 1
print("Nice" if want == N + 1 else "Sad")