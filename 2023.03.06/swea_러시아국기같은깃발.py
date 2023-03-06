# SW Expert Academy - 4613 러시아 국기 같은 깃발

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M  = map(int, input().split())
    flag = [input() for _ in range(N)]
    min_val = N*M
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for k in range(i+1):
                for l in range(M):
                    if flag[k][l] != 'W':
                        cnt += 1
            for k in range(i+1, j+1):
                for l in range(M):
                    if flag[k][l] != 'B':
                        cnt += 1
            for k in range(j+1, N):
                for l in range(M):
                    if flag[k][l] != 'R':
                        cnt += 1
            if cnt < min_val:
                min_val = cnt
    print(f'#{t}', min_val)
