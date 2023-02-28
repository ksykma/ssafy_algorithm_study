# SW Expert Academy - 11315   

import sys
sys.stdin = open('input.txt', 'r')

def omok(r, c, cnt):
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]   # 상하좌우, 대각
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(8):
        count = 0
        for j in range(cnt):
            nr = r + dr[i] * j
            nc = c + dc[i] * j
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'o':
                    count += 1
        if count == 5:
            return 1
    else:
        return 0
            
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += omok(i, j, 5)
    if ans != 0:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')