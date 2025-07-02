N,M = map(int,input().split())
board = [input().strip() for _ in range(N)]

min_repaints = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        repaint_count1 = 0
        repaint_count2 = 0
        
        for x in range(8):
            for y in range(8):
                expected_color1 = 'W' if (x+y) % 2 == 0 else 'B'
                expected_color2 = 'B' if (x+y) % 2 == 0 else 'W'
                if board[i+x][j+y] != expected_color1:
                    repaint_count1 += 1
                if board[i+x][j+y] != expected_color2:
                    repaint_count2 += 1
        min_repaints = min(min_repaints,repaint_count1, repaint_count2)
print(min_repaints)