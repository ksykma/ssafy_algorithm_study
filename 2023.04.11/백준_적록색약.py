# 백준 10026 적록색약

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
drawing = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
Q = []
ans1 = 0
ans2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        cnt = 0
        Q.append((i, j))
        while Q:
            r, c = Q.pop(0)
            if visited[r][c] == 1:
                continue
            cnt += 1
            visited[r][c] = 1
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if drawing[nr][nc] == drawing[r][c]:
                        Q.append((nr, nc))
        if cnt != 0:
            ans1 += 1
            
for i in range(N):
    for j in range(N):
        if drawing[i][j] == 'R':
            drawing[i][j] = 'G'

visited = [[0]*N for _ in range(N)]            
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        cnt = 0
        Q.append((i, j))
        while Q:
            r, c = Q.pop(0)
            if visited[r][c] == 1:
                continue
            cnt += 1
            visited[r][c] = 1
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if drawing[nr][nc] == drawing[r][c]:
                        Q.append((nr, nc))
        if cnt != 0:
            ans2 += 1
print(ans1)
print(ans2)