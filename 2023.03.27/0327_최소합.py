# SW Expert Academy 0227_Start - 완전검색_최소합

import sys
sys.stdin = open('input.txt', 'r')


def function(r, c, cnt):
    global ans
    cnt += arr[r][c]
    if ans < cnt:
        return
    if r == N-1 and c == N-1:
        if ans > cnt:
            ans = cnt
        return
    dr = [1, 0] # 하, 우
    dc = [0, 1]
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            function(nr, nc, cnt)
    

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10000
    function(0, 0, 0)
    print(f'#{t} {ans}')
