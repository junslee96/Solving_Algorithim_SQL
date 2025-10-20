import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

tmp = [0] * N  # 전역 임시 배열 재사용
cnt = 0        # 지금까지의 저장(=A에의 대입) 횟수
answer = -1    # K번째 저장되는 수 (기본값 -1)

def merge_sort(l, r):
    if l >= r:
        return
    m = (l + r) // 2
    merge_sort(l, m)
    merge_sort(m + 1, r)
    merge(l, m, r)

def merge(l, m, r):
    # 1) l..m, m+1..r 두 구간을 tmp에 병합(오름차순)
    i, j, t = l, m + 1, l
    while i <= m and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
    while i <= m:
        tmp[t] = A[i]
        i += 1
        t += 1
    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1

    # 2) tmp[l..r]을 A[l..r]에 "저장" (여기가 저장 카운트 지점)
    global cnt, answer
    for i in range(l, r + 1):
        A[i] = tmp[i]
        cnt += 1
        if cnt == K:
            answer = A[i]

merge_sort(0, N - 1)
print(answer)
