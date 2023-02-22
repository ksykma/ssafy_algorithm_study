 # SW Expert Academy 0221_Queue - 1226

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(1, 11):
    T = int(input())
    miro = [list(input()) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    Q = deque([])
    visited[1][1] = 1
    Q.append((1, 1))
    result = 0
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if visited[nr][nc] == 0:
                    if miro[nr][nc] == '0':
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append((nr, nc))
                    elif miro[nr][nc] == '3':
                        result = 1
    print(f'#{t}', result)
