# 백준 2589 보물섬

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
treasure = [list(input()) for _ in range(N)]
lst = []
for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'L':
            lst.append((i, j))
Q = []
ans = 0
for i in range(len(lst)):
    visited = [[0]*M for _ in range(N)]
    Q.append(lst[i])
    a, b = lst[i]
    visited[a][b] = 1
    while Q:
        r, c = Q.pop(0)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if 0 <= nr < N and 0 <= nc < M:
                if treasure[nr][nc] == 'L' and not visited[nr][nc]:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    for j in range(N):
        if ans < max(visited[j]):
            ans = max(visited[j])
                      
print(ans-1)