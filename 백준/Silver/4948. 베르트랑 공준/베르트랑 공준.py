import sys
import math
input = sys.stdin.readline


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False
    return is_prime

while True:
    n = int(input().strip())
    if n == 0:
        break
    is_prime = sieve(2*n)
    count = sum(1 for i in range(n+1, 2*n+1) if is_prime[i])
    print(count)
    