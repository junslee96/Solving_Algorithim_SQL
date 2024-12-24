def factorial(num):
    a=1
    for i in range(1,num+1):
        a *= i
    return a

def solution(balls, share):
    answer = 0
    numer = factorial(balls)
    denom = factorial(balls-share)*factorial(share)
    answer = numer/denom
    return answer