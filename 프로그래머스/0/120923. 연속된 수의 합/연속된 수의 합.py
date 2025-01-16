def solution(num, total):
    mid = total // num
    answer = []
    if total % num == 0:
        start = mid - num//2
        return [start + i for i in range(num)]
    else :
        start = mid - num//2 +1
        return [start + i for i in range(num)]