import sys
input = sys.stdin.readline
n = int(input())

def hanoi(k, a, b, c, out):
    if k == 0:
        return
    hanoi(k-1, a, c, b, out)
    out.write(F"{a} {c}\n")
    hanoi(k-1, b, a, c, out)

total_moves = (1 << n) - 1
print(total_moves)

hanoi(n, 1, 2, 3, sys.stdout)