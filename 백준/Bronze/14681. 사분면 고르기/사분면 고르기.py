#두 정수 각각 입력
X=int(input())
Y=int(input())
#X와Y의 범위에 따라 사분면 조건 설정
if X>=0 and Y>=0:
    print(1)
elif X<0 and Y>=0:
    print(2)
elif X<0 and Y<0:
    print(3)
else:
    print(4)