import sys
input = sys.stdin.readline

def recursion(s, l, r, c):
    c[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1, c)
    
def isPalindrome(s, c):
    return recursion(s, 0, len(s)-1, c)

T = int(input())
for _ in range(T):
    s = input().strip()
    c = [0]
    result = isPalindrome(s, c)
    print(result, c[0])
    