import sys
input=sys.stdin.readline
#테스트케이스의 개수 T
T=int(input())
#1부터T까지 for문
for i in range(1,T+1):
    A,B=map(int,input().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")