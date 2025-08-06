import sys
input = sys.stdin.readline

A,B = map(int,input().split())
set_A = set(map(int,input().split()))
set_B = set(map(int,input().split()))
set_AminusB = set_A - set_B
set_BminusA = set_B - set_A
print(len(set_AminusB)+len(set_BminusA))