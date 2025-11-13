import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int,input().split()))
plus,minus,mul,div = map(int,input().split())

max_value = -10**9 - 1
min_value = 10**9 + 1

def my_div(a,b):
    if a >= 0:
        return a//b
    else:
        return -(-a//b)

def dfs(idx, value, p, m, mu, d):
    global max_value, min_value
    
    if idx == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return
    next_num = nums[idx]
    if p > 0:
        dfs(idx + 1, value + next_num, p - 1, m, mu, d)
    if m > 0:
        dfs(idx + 1, value - next_num, p, m -1, mu, d)
    if mu > 0:
        dfs(idx + 1, value * next_num, p, m, mu - 1, d)
    if d > 0:
        dfs(idx + 1, my_div(value, next_num), p, m, mu, d - 1)
dfs(1, nums[0], plus, minus, mul, div)

print(max_value)
print(min_value)