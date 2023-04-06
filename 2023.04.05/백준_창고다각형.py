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


result = max_bar
for i in range(max_idx):
    if lst[i+1][1] > lst[i][1]:
        result += (lst[i+1][0]-lst[i][0])*lst[i][1]
    else:
        result += (lst[i+1][0]-lst[i][0])*lst[i][1]
        lst[i+1][1] = lst[i][1]

for i in range(N-1, max_idx, -1):
    if lst[i-1][1] > lst[i][1]:
        result += (lst[i][0]-lst[i-1][0])*lst[i][1]
    else:
        result += (lst[i][0]-lst[i-1][0])*lst[i][1]
        lst[i-1][1] = lst[i][1]

print(result)
