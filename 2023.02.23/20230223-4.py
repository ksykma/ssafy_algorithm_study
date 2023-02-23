# SW Expert Academy 0223_Tree - 12916   

import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = []
    for i in nums:
        heappush(heap, i)
    result = 0
    number = N
    while number != 1:
        number = number // 2
        result += heap[number-1]
    print(f'#{t}', result)

