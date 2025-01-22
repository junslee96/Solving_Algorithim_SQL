N=int(input())
count=N//4
result=""
#count만큼만 반복
for _ in range(count):
    result+="long "
result+="int"
print(result)
