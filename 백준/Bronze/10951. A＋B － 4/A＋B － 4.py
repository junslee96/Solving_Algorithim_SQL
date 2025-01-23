import sys

for i in sys.stdin:
    A,B=map(int,i.split())
    if A==0 and B==0:
        break
    print(A+B)