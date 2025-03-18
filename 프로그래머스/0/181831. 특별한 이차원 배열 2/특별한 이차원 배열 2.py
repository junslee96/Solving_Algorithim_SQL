def solution(arr):
    n = len(arr)
    return 1 if all(arr[i][j]==arr[j][i] for i in range(n) for j in range(n)) else 0