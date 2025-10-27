import sys

input = sys.stdin.readline
N,M = map(int,input().split())

path = []
out = []

def dfs(start: int):
    if len(path) == M:
        out.append(" ".join(map(str,path)))
        return
    for x in range(start,N+1):
        path.append(x)
        dfs(x+1)
        path.pop()

dfs(1)
sys.stdout.write("\n".join(out))