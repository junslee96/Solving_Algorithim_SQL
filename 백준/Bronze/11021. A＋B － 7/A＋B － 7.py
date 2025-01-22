import sys
input=sys.stdin.readline
#첫줄에테스트케이스로 개수T입력
T=int(input())
#각테스트케이스마다 A,B를 입력받아 gkq 계산
for i in range(1,T+1):
    A,B=map(int,input().split())
    print(f"Case #{i}: {A+B}")

