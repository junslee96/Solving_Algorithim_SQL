import sys

input = sys.stdin.readline
N,M = map(int,input().split())

path = []
out = []

def dfs():
    if len(path) == M:
        out.append(" ".join(map(str,path)))
        return
    for x in range(1,N+1):
        path.append(x)
        dfs()
        path.pop()
dfs()
sys.stdout.write("\n".join(out))