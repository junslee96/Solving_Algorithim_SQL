import sys
input = sys.stdin.readline
#첫 줄에 테스트케이스의 개수 T입력
T=int(input().strip())
#결과 저장할 리스트
result =[]
#각 테스트케이스마다 A,B 입력받고 합 계산
for _ in range(T):
    A,B=map(int,input().split())
    result.append(A+B)    
#한 번에 출력
sys.stdout.write("\n".join(map(str,result))+"\n")