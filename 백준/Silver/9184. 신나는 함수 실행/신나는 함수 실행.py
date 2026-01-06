import sys
input = sys.stdin.readline

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
vis = [[[False] * 21 for _ in range(21)] for _ in range(21)]

def w(a: int, b: int, c: int) -> int:
    # base
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # clamp
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if vis[a][b][c]:
        return dp[a][b][c]
    vis[a][b][c] = True

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )
    return dp[a][b][c]

out = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    out.append(f"w({a}, {b}, {c}) = {w(a, b, c)}")

print("\n".join(out))
