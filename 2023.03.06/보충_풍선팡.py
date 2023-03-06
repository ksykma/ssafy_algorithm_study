# SW Expert Academy 0302 - 9490 풍선팡

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
                for l in range(1, flower[i][j]+1):
                    nr = i + dr[k]*l
                    nc = j + dc[k]*l
                    if 0 <= nr < N and 0 <= nc < M:
                        cnt += flower[nr][nc]
            if max_val < cnt:
                max_val = cnt
    print(f'#{t}', max_val)