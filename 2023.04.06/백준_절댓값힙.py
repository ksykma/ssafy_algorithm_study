# 백준 11286 절댓값 힙

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
lst = []
for i in range(N):
    x = int(input())
    if x != 0:
        if x > 0:
            heappush(lst, (x, 1))
        else:
            heappush(lst, (-x, -1))
    else:
        if not lst:
            print(0)
        else:
            ans, check = heappop(lst)
            if check == 1:
                print(ans)
            else:
                print(-ans)