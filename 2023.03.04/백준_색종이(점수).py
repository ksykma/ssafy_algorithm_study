# 백준 10163 색종이

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*1001 for _ in range(1001)]
for i in range(N):
    c, r, w, h = paper[i]
    for j in range(h):
        for k in range(w):
            arr[1000-c-k][r+j] = i+1
n = 1
while n != N+1:
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == n:
                cnt += 1
    n += 1
    print(cnt)