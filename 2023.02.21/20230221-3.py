# SW Expert Academy 0221_Queue - 11652

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 1은 벽, 2는 출발, 3은 도착
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':   # 값이 2인 곳 추출
                r = i
                c = j
    visited = [[0] * N for _ in range(N)]   # 방문여부 검사
    Q = deque([])
    Q.append((r, c))   # 시작 장소 넣어놓기
    visited[r][c] = 1   # 시작 장소 방문여부 넣어놓기
    result = 0
    while Q:
        r, c = Q.popleft()   # 시작 장소 뽑아
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0:   # 방문 안한 곳
                    if arr[nr][nc] == '0':   # 값이 0이
                        Q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1
                    elif arr[nr][nc] == '3':
                        visited[nr][nc] = visited[r][c] + 1
                        result = visited[nr][nc] - 2
    print(f'#{t}', result)
    
