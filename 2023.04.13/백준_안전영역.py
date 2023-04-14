# 백준 2468 안전 영역

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def func():
    while Q:
        r, c = Q.popleft()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for l in range(4):
            nr = r + dr[l]
            nc = c + dc[l]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] > i and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min_val = 0xfffff
max_val = 0
for i in range(N):
    for j in range(N):
        if board[i][j] < min_val:
            min_val = board[i][j]
        if board[i][j] > max_val:
            max_val = board[i][j] 
ans = 0
Q = deque()
for i in range(min_val, max_val):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if board[j][k] > i and not visited[j][k]:
                Q.append((j, k))
                visited[j][k] = 1
                cnt += 1
                func()
    if cnt > ans:
        ans = cnt
if ans == 0:
    print(1)
else:
    print(ans)           