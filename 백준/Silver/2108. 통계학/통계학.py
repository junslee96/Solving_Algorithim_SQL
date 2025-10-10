import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
nums = list(int(input()) for _ in range(N))
# 1) 산술 평균
avg = round(sum(nums)/N)
# 2) 중앙값
nums.sort()
median = nums[N//2]
# 3) 최빈값
cnt = Counter(nums)
max_freq = max(cnt.values())
modes = [x for x, f in cnt.items() if f == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]
# 4) 범위
rng = nums[-1] - nums[0]

print(avg)
print(median)
print(mode)
print(rng)