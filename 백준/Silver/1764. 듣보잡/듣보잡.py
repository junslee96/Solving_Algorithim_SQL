import sys
input = sys.stdin.readline

N,M = map(int,input().split())
never_heard = set(input().strip() for _ in range(N))
never_seen = set(input().strip() for _ in range(M))

never_heard_seen = sorted(never_heard & never_seen)

print(len(never_heard_seen))
print('\n'.join(never_heard_seen))