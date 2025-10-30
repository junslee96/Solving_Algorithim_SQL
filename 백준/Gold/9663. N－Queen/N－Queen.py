import sys
input = sys.stdin.readline

def main():
    N = int(input().strip())
    ALL = (1 << N) - 1  # N비트 1

    # cols: 점유 열, d1: 좌상향 대각선, d2: 우상향 대각선
    def dfs(cols: int, d1: int, d2: int) -> int:
        if cols == ALL:
            return 1
        cnt = 0
        # 현재 행에서 놓을 수 있는 모든 자리(비트)
        avail = ALL & ~(cols | d1 | d2)
        while avail:
            p = avail & -avail      # 최하위 1비트 선택
            avail -= p
            cnt += dfs(cols | p,
                      (d1 | p) << 1 & ALL,
                      (d2 | p) >> 1)
        return cnt

    # 대칭 최적화: 0행의 좌절만 세고 *2, 홀수면 중앙 열은 따로 한 번
    total = 0
    half = N // 2
    for c in range(half):
        p = 1 << c
        total += dfs(p, (p << 1) & ALL, (p >> 1))
    total *= 2
    if N % 2 == 1:
        p = 1 << (N // 2)
        total += dfs(p, (p << 1) & ALL, (p >> 1))

    print(total)

if __name__ == "__main__":
    main()
