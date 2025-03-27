n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
matrix_map = [[0]*100 for _ in range(100)]
for x,y in matrix:
    for i in range(y,y+10):
        for j in range(x, x+10):
            matrix_map[i][j] = 1
            
demension = sum(sum(row) for row in matrix_map)
print(demension)    
    