#현재시각 입력
H,M=map(int,input().split())
#요리시간 입력
time=int(input())
cook_M=M+time
#분이 60이상일때
if cook_M >=60:
    H+=cook_M//60
    cook_M%=60
#시간이 24이상일때
if H>=24:
    H-=24
print(H,cook_M)