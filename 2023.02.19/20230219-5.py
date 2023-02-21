# SW Expert Academy 0217_문제풀이3 - 10760

import sys
sys.stdin = open('input.txt', 'r')

def function(r, c):
    global result
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    cnt = 0
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if char[nr][nc] < char[r][c]:
                cnt += 1
    if cnt >= 4:
        result += 1

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    char = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            function(i, j)
    print(result)