# 백준 1012 유기농 배추

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    baechu = [[0]*M for _ in range(N)]
    for i in range(K):
        c, r = map(int, input().split())
        baechu[r][c] = 1
    Q = []
    ans = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 1:
                if visited[i][j] == 1:
                    continue
                Q.append((i, j))
                while Q:
                    r, c = Q.pop(0)
                    dr = [-1, 1, 0, 0]
                    dc = [0, 0, -1, 1]
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < M:
                            if baechu[nr][nc] == 1:
                                if visited[nr][nc] == 1:
                                    continue
                                visited[nr][nc] = 1
                                Q.append((nr, nc))
                ans += 1
    print(ans)
                