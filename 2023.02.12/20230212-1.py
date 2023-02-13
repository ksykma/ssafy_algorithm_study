# SW Expert Academy 0210_문제풀이2 - 1979

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    a = 0
    result = 0
    # 가로 확인
    while a < N:
        for i in range(N):
            cnt = 0
            for j in range(N):
                if lst[i][j] == 1:
                    cnt += 1
                elif lst[i][j] == 0:
                    if cnt == K:
                        result += 1
                    cnt = 0
                    continue
            if cnt == K:
                result += 1
            a += 1
        a = 0
        # 세로 확인
        while a < N:
            for i in range(N):
                cnt = 0
                for j in range(N):
                    if lst[j][i] == 1:
                        cnt += 1
                    elif lst[j][i] == 0:
                        if cnt == K:
                            result += 1
                        cnt = 0
                        continue
                if cnt == K:
                    result += 1
                a += 1
    print(f'#{t} {result}')
