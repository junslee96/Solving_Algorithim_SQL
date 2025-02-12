def solution(n):
    sum = 0
    if n % 2 == 0:
        for i in range(1,n//2+1):
            sum += i*2*i*2
        return sum
    else:
        for i in range(1,n//2+2):
            sum += i*2-1
        return sum