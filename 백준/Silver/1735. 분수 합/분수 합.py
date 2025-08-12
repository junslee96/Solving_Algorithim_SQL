import sys
import math
input = sys.stdin.readline

A_num,A_den = map(int,input().split())
B_num,B_den = map(int,input().split())

num = A_num*B_den + A_den*B_num
den = B_den*A_den

gcd = math.gcd(num,den)
num //= gcd
den //= gcd
print(num,den)