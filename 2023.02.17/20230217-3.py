# SW Expert Academy 0217_문제풀이3 - 10760

import sys
sys.stdin = open('input.txt', 'r')

def function(r, c):
    global result
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]
    lr = [-1, -1, 1, 1]   # 대각선
    lc = [-1, 1, -1, 1]
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        mr = r + lr[i]
        mc = c + lc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] < arr[r][c]:
                cnt += 1
        if 0 <= mr < N and 0 <= mc < M:
            if arr[mr][mc] < arr[r][c]:
                cnt += 1
    if cnt >= 4:
        result += 1

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for row in range(N):
        for col in range(M):
            function(row, col)
    print(f'#{t}', result)
