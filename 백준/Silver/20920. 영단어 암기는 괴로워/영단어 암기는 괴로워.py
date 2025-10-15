import sys
from collections import Counter
input = sys.stdin.readline

N,M = map(int,input().split())
freq = Counter()
for _ in range(N):
    w = input().strip()
    if len(w) >= M:
        freq[w] += 1
w_sorted = sorted(freq.keys(), key=lambda w: (-freq[w], -len(w), w))
print("\n".join(w_sorted))    