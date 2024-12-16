def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b,a%b)
def solution(n):
    # 최소공배수 / 6
    # lcm = a*b/gcd
    a = n
    b = 6
    lcm =  a*b/gcd(a,b)
    answer = lcm / 6
    return answer