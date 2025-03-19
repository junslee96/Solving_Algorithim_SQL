black = [1,1,2,2,2,8]
white = list(map(int,input().split()))
diff = [a-b for a,b in zip(black,white)]
print(*diff)