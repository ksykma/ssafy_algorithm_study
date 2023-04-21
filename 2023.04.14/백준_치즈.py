# 백준 2636 치즈

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
total = 0
for i in range(N):
    total += cheeze[i].count(1)
    
while True:
    Q = [(0, 0)]
    visited = [[0]*M for _ in range(N)]
    melted = []
    while Q:
        r, c = Q.pop(0)
        visited[r][c] = 1
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0:
                    if cheeze[nr][nc] == 0:
                        Q.append((nr, nc))
                        visited[nr][nc] = 1
                    else:
                        melted.append((nr, nc))
                        visited[nr][nc] = 1
    once = len(melted)                    
    for i in range(once):
        a, b = melted[i]
        cheeze[a][b] = 0
    cnt += 1
    total -= once
    if total == 0:
        print(cnt)
        print(once)
        break