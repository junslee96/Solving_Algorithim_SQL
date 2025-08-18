import sys

#에라토스테네스의 체
def sieve(n: int): # ': int' : 타입 힌트, 문법적 주석
    is_prime=[True]*(n+1)
    is_prime[0] = is_prime[1] = False
    
    import math
    limit = int(math.isqrt(n)) #istqrt: 정수 제곱근(integer square root)
    for p in range(2,limit+1):
        if is_prime[p]:
            step = p
            start = p*p
            is_prime[start:n+1:step]=[False]*(((n-start)//step)+1)
    return is_prime

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    Ns = [int(input().strip()) for _ in range(T)]
    M = max(Ns)
    is_prime = sieve(M) # 최댓값으로 세팅해서 시간 절약
    
    out_lines = []
    for N in Ns:
        cnt = 0
        half = N // 2
        for p in range(2, half + 1):
            if is_prime[p] and is_prime[N - p]:
                cnt += 1
        out_lines.append(str(cnt))
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == "__main__":
    main()