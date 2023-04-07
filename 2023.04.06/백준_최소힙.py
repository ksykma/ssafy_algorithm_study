# 백준 1927 최소 힙

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
lst = []
for i in range(N):
    x = int(input())
    if x:
        heappush(lst, x)
        continue
    if not lst:
        print(0)
    else:
        print(heappop(lst))
