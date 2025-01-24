#N:바구니 수,M:바꿀 횟수
N,M=map(int,input().split())
#바구니 초기 번호 설정
baskets=list(range(1,N+1))
#M개의 교환 작업 수행
for _ in range(M):
    i,j=map(int,input().split())
    #i바구니와 j바구니의 번호 교환
    baskets[i-1],baskets[j-1]=baskets[j-1],baskets[i-1]
print(*baskets)
    