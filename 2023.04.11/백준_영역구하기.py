# 백준 2583 영역 구하기

import sys
sys.stdin = open('input.txt', 'r')

M, N, K = map(int, input().split())
paper = [[0]*N for _ in range(M)]
for i in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for j in range(r1, r2):
        for k in range(c1, c2):
            paper[j][k] = 1
visited = [[0]*N for _ in range(M)]
Q = []
ans = 0
result = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            if visited[i][j] == 1:
                continue
            cnt = 0
            Q.append((i, j))
            while Q:
                r, c = Q.pop(0)
                cnt += 1
                visited[r][c] = 1
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < M and 0 <= nc < N:
                        if paper[nr][nc] == 0:
                            if visited[nr][nc] == 1:
                                continue
                            visited[nr][nc] = 1
                            Q.append((nr, nc))
            ans += 1
            result.append(cnt)
result.sort()
print(ans)
print(*result)