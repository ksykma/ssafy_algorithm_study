# 백준 2304 창고 다각형

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
max_bar = 0
max_idx = 0
for i in range(N):
    if lst[i][1] > max_bar:
        max_bar = lst[i][1]
        max_idx = i
left = lst[:max_idx]
right = lst [max_idx+1:]
for i in range(len(left)-1, -1, -1):
    if len(left) >= 2:
        if left[i][1] < left[i-1][1]:
            left[i][1] = 0
for i in range(len(right)-1):
    if len(right) >= 2:
        if right[i][1] < right[i+1][1]:
            right[i][1] = 0


