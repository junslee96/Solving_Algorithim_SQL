#세 정수 입력
A,B,C=map(int,input().split())
#(A+B)%C 출력
print((A+B)%C)
#((A%C)+(B%C))%C 출력
print(((A%C)+(B%C))%C)
#(A*B)%C 출력
print((A*B)%C)
#((A%C)*(B%C))%C 출력
print(((A%C)*(B%C))%C)