# 백준 2206 벽 부수고 이동하기

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
room = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
Q = [(0, 0, 1)]
visited[0][0][1] = 1
while Q:
    r, c, wall = Q.pop(0)
    # if r == N-1 and c == M-1:
    #     print(visited[r][c][wall])
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if room[nr][nc] == 0 and visited[nr][nc][wall] == 0:
                Q.append((nr, nc, wall))
                visited[nr][nc][wall] = visited[r][c][wall] + 1
            if room[nr][nc] == 1 and wall == 1:
                Q.append((nr, nc, wall - 1))
                visited[nr][nc][wall-1] = visited[r][c][wall] + 1
if visited[N-1][M-1][wall] == 0:
    print(-1)
else:
    print(visited[N-1][M-1][wall])