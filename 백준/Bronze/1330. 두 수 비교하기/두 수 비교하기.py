#두 정수 입력
A,B = map(int,input().split())
#세 가지 경우 비교
if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")