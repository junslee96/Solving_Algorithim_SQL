N,X=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for num in A:
    if num < X:
        B.append(num)
print(*B)