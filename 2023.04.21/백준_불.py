# 백준 5427 불

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while Q:
        r, c = Q.popleft()
        if visited[r][c] != '*':
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if visited[nr][nc] == 0 and building[nr][nc] == '.':
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append((nr, nc))
                else:
                    return visited[r][c]
        else:
            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]
                if 0 <= nr < h and 0 <= nc < w:
                    if building[nr][nc] == '.' or building[nr][nc] == '@':
                        building[nr][nc] = '*'
                        visited[nr][nc] = '*'
                        Q.append((nr, nc))
    else:
        return 'IMPOSSIBLE'

N = int(input())
for t in range(N):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    Q = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                Q.insert(0, (i, j))
                visited[i][j] = 1
            if building[i][j] == '*':
                Q.append((i, j))
                visited[i][j] = '*'
    print(bfs())

            
    # for line in visited:
    #     print(*line)
    # print(nr, nc)
    # for line in building:
    #     print(*line)   
    
    # if nr in [0, h-1] or nc in [0, w-1]:
    #     print(visited[nr][nc])
    # else:
    #     print('IMPOSSIBLE')
