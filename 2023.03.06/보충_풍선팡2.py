# SW Expert Academy 0302 - 16268 풍선팡2

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N):
        for j in range(M):
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            cnt = 0
            cnt += flower[i][j]
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    cnt += flower[nr][nc]
            if max_val < cnt:
                max_val = cnt
    print(f'#{t}', max_val)