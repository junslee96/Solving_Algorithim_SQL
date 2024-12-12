def gcd(a,b): #최대공약수 정의 (gcd:greatest common divisor)
    if a%b==0:
        return b
    return gcd(b,a%b)

def solution(numer1, denom1, numer2, denom2): # 분자: numerator, 분모: denominator
    # 두 분수의 합을 계산한 후 분자, 분모 계산
    denom = denom1 * denom2
    numer = denom1*numer2+numer1*denom2
    # 최대공약수 계산
    gcd_value = gcd(numer,denom)
    # 최대공약수로 약분하여 기약분수 만들기
    answer = [numer/gcd_value, denom/gcd_value]
    return answer