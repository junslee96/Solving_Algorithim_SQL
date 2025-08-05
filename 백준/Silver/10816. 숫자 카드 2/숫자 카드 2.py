import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))

card_counter = Counter(cards)

M = int(input())
queries = list(map(int,input().split()))

result = [str(card_counter[q]) for q in queries]
print(' '.join(result))