import sys
input = sys.stdin.readline

N = int(input())
measure = list(map(int,input().split()))
print(min(measure)*max(measure))