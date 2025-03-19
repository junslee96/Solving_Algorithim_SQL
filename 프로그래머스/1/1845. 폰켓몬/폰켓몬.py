def solution(nums):
    n = len(nums)
    nums = set(nums)
    if len(nums) <= n // 2:
        return len(nums)
    return n//2