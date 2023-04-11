# 백준 7576 토마토

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def tomato(r, c, check):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc] == 1:
                continue
            if box[nr][nc] == 0:
                box[nr][nc] = 1
                visited[nr][nc] = 1
                Q.append((nr, nc, check+1))
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            Q.append((i, j, 0))
            
visited = [[0]*M for _ in range(N)]
cnt = 0
while Q:
    r, c, check = Q.popleft()
    visited[r][c] = 1
    cnt = check
    tomato(r, c, check)

for i in range(N):
    if 0 in box[i]:
        cnt = -1
        break
        
print(cnt)
