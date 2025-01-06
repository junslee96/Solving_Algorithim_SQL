def solution(num, k):
    num = str(num)
    k = str(k)
    if k not in num:
        return -1
    else:
        return num.index(k)+1