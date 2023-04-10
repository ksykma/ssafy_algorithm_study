# SW Expert Academy 1249. [S/W 문제해결 응용] 4일차 - 보급로

import sys
sys.stdin = open('input.txt', 'r')

def war(r, c):
    cnt = 0xfffff
    idx = (0, 0)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if int(war_map[nr][nc]) < cnt:
                cnt = int(war_map[nr][nc])
                idx = (nr, nc)
    return cnt, idx
            
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    war_map = [list(input()) for _ in range(N)]
    Q = [(0, 0)] # r, c
    D = [[0xfffff]*(N) for _ in range(N)]
    D[0][0] = 0
    while Q:
        d, r, c = Q.pop(0)
        a, (b, c) = war(r, c)
        D[b][c] = D[r][c] + a
        