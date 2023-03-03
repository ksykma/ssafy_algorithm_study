# SW Expert Academy 0303_문제풀이5 - 12712

import sys
sys.stdin = open('input.txt', 'r')

def function(r, c, m):
    dr = [-1, 1, 0, 0] # 상하좌우
    dc = [0, 0, -1, 1]
    cr = [-1, -1, 1, 1] # 대각선
    cc = [-1, 1, -1, 1]
    cnt1 = 0
    cnt2 = 0
    for i in range(4):
        for j in range(m):
            nr = r + dr[i] * j
            nc = c + dc[i] * j
            rr = r + cr[i] * j
            rc = c + cc[i] * j
            if 0 <= nr < N and 0 <= nc < N:
                cnt1 += arr[nr][nc]
            if 0 <= rr < N and 0 <= rc < N:
                cnt2 += arr[rr][rc]
    cnt1 -= arr[r][c] * 3
    cnt2 -= arr[r][c] * 3
    return max(cnt1, cnt2)

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            result.append(function(i, j, M))
    print(f'#{t}', max(result))