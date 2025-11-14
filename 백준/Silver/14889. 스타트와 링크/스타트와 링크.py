import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
S = [list(map(int,input().split())) for _ in range(N)]

pair = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        pair[i][j] = S[i][j] + S[j][i]

min_diff = float('inf')
selected = [False] * N

def calc(team):
    total = 0
    m = len(team)
    for i in range(m):
        for j in range(i+1,m):
            a = team[i]
            b = team[j]
            if a < b:
                total += pair[a][b]
            else:
                total += pair[b][a]
    return total

def dfs(idx, cnt):
    global min_diff
    
    if cnt == N // 2:
        start = [i for i in range(N) if selected[i]]
        link = [i for i in range(N) if not selected[i]]
        
        start_score = calc(start)
        link_score = calc(link)
        diff = abs(start_score - link_score)
        
        if diff == 0:
            print(0)
            sys.exit(0)
        if diff < min_diff:
            min_diff = diff
        return
    
    if idx == N:
        return
    if N - idx < (N // 2 - cnt):
        return
    
    selected[idx] = True
    dfs(idx + 1, cnt + 1)
    
    selected[idx] = False
    dfs(idx + 1, cnt)
dfs(0,0)
print(min_diff)
