# 백준 2563 색종이

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [[0]*100 for _ in range(100)]
for i in range(N):
    color = list(map(int, input().split()))
    r = color[1]
    c = color[0]
    for i in range(c, c+10):
        for j in range(r, r+10):
            arr[i][j] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > 1:
            cnt += 1
print(cnt)
