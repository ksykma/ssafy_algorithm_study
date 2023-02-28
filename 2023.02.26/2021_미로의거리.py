# SW Expert Academy 0221_Queue - 11652    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                r = i
                c = j
    Q = [[r, c]]
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    result = 0
    while Q:
        r, c = Q.pop(0)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0:
                    if arr[nr][nc] == '0':
                        Q.append([nr, nc])
                        visited[nr][nc] = visited[r][c] + 1
                    elif arr[nr][nc] == '3':
                        visited[nr][nc] = visited[r][c] + 1
                        result = visited[nr][nc] - 2
    print(f'#{t}', result)