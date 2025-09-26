import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
q = deque()
out = []
for _ in range(N):
    parts = input().split()
    cmd = int(parts[0])
    
    if cmd == 1:
        q.appendleft(int(parts[1]))
    elif cmd == 2:
        q.append(int(parts[1]))
    elif cmd == 3:
        out.append(str(q.popleft() if q else -1))
    elif cmd == 4:
        out.append(str(q.pop() if q else -1))
    elif cmd == 5:
        out.append(str(len(q)))
    elif cmd == 6:
        out.append('1' if not q else '0')
    elif cmd == 7:
        out.append(str(q[0] if q else -1))
    elif cmd == 8:
        out.append(str((q[-1] if q else -1)))

write('\n'.join(out))                   