a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
is_valid = True
for n in range(n0, 101):
    if a1 * n + a0 > c * n:
        is_valid = False
        break
print(1 if is_valid else 0)