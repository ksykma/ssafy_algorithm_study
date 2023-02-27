# SW Expert Academy List(Array)_조작하기 - 10989    

import sys
sys.stdin = open('input.txt', 'r')

def war(r, c, b):
    dr = [-1, 1, 0, 0]   # 상하좌우
    dc = [0, 0, -1, 1]
    result = 0
    result += arr[r][c]
    lst[r][c] += 1 
    for i in range(4):
        for j in range(1, b+1):
            nr = r + dr[i] * j
            nc = c + dc[i] * j
            if 0 <= nr < N and 0 <= nc < N:
                result += arr[nr][nc]
                lst[nr][nc] += 1 
    return result
T = int(input())
for t in range(1, T + 1):
    # N은 지도의 크기, M은 폭탄의 수
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(M):
        raw, column, bomb = list(map(int, input().split()))
        ans += war(raw, column, bomb)
    for i in range(N):
        for j in range(N):
            if lst[i][j] > 1:
                ans -= arr[i][j] * (lst[i][j] - 1)
    print(f'#{t}', ans)
    