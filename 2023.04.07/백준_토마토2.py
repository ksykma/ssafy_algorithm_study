# 백준 7569 토마토2

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def tomato(h, r, c, check):
    dh = [-1, 1, 0, 0, 0, 0]
    dr = [0, 0, -1, 1, 0, 0] # 상하앞뒤좌우
    dc = [0, 0, 0, 0, -1, 1]
    for i in range(6):
        nh = h + dh[i]
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
            if visited[nh][nr][nc] == 1:
                continue
            if box[nh][nr][nc] == 0:
                box[nh][nr][nc] = 1
                visited[nh][nr][nc] = 1
                Q.append((nh, nr, nc, check+1))
M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]
Q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                Q.append((h, n, m, 0))

visited = [[[0]*M for i in range(N)] for j in range(H)]

cnt = 0
while Q:
    h, r, c, check = Q.popleft()
    visited[h][r][c] = 1
    cnt = check
    tomato(h, r, c, check)

for i in range(H):
    for j in range(N):
        if 0 in box[i][j]:
            cnt = -1
            break
        
print(cnt)
