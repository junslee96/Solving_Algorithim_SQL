import sys

input = sys.stdin.readline
N = int(input())
array = list(int(input()) for _ in range(N))
array.sort()
sys.stdout.write('\n'.join(map(str,array))+'\n')