#세 정수 입력
a,b,c=map(int,input().split())
prize=0
#같은눈1개
if a == b == c:
    prize = 10000 + (a * 1000)
#같은눈2개  
elif a == b or b == c or a == c: 
    if a == b or a == c: 
        prize = 1000 + (a * 100)
    else:  
        prize = 1000 + (b * 100)
#모두다른눈        
else: 
    prize = max(a, b, c) * 100
print(prize)