import sys
import math

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    print(math.isqrt(N))
    
if __name__=="__main__":
    main()