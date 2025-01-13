def solution(a, b):
    # 최대 공약수
    def gcd(x,y):
        while y:
            x,y=y,x%y
        return x
    # 기약분수
    g = gcd(a,b)
    a //=g
    b //=g
    # 분모의 소인수 2,5
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    # 소인수가 다른 값이면 2 반환
    return 1 if b == 1 else 2
