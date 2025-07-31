import sys
input = sys.stdin.readline

n = int(input())
company = dict()
for _ in range(n):
    name,status = input().split()
    if status == 'enter':
        company[name] = True
    elif status == 'leave':
        del company[name]
for name in sorted(company.keys(), reverse=True):
    print(name)

    