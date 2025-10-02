import math
N,K = map(int,input().split())
numer = math.factorial(N)
denum = math.factorial(K)*math.factorial(N-K)
print(numer//denum)