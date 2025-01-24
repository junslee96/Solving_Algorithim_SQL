#N:바구니 개수,M:작업 개수
N,M=map(int,input().split())
#바구니 초기화(1번부터 N번까지 모두)
baskets=[0]*N
#M개의 작업 수행
for _ in range(M):
    i,j,k = map(int,input().split())
    for idx in range(i-1,j):
        baskets[idx]=k
print(*baskets)