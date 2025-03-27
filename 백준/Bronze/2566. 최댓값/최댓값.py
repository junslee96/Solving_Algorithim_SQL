grid = [list(map(int,input().split())) for _ in range(9)]
max_value = max(max(row) for row in grid)
max_position = [(i+1, row.index(max_value) + 1) for i, row in enumerate(grid) if max_value in row][0]
print(max_value)
print(*max_position)   