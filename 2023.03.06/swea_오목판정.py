# SW Expert Academy - 16811 당근 포장하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            for k in range(8):
                cnt = 0
                for l in range(5):
                    nr = i + dr[k] * l
                    nc = j + dc[k] * l
                    if 0 <= nr < N and 0 <= nc < N:
                        if omok[nr][nc] == 'o':
                            cnt += 1
                if cnt == 5:
                    result = 'YES'
                    break
            if result == 'YES':
                break
        if result == 'YES':
                break
    print(f'#{t}', result)