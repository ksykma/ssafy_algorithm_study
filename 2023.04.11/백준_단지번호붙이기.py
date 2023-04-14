# 백준 2667 단지번호붙이기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
danji = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
Q = []
result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == '1':
            continue
        if danji[i][j] == '1':
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
                        if danji[nr][nc] == '1':
                            Q.append((nr, nc))
            if cnt != 0:
                result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)