import sys

input = sys.stdin.readline
N=int(input())
X=list(map(int,input().split()))

sorted_X=sorted(set(X))
X_dict={value: idx for idx, value in enumerate(sorted_X)}

answer = [X_dict[x] for x in X]
print(*answer)