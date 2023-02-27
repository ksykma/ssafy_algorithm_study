# SW Expert Academy List(Array)_조작하기 - 11014    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(1, N):   # 가로
        for j in range(1, N):   # 세로
            a = 0
            b = 0
            c = 0
            for k in range(i):
                for l in range(j):
                    a += farm[k][l]
            for k in range(i, N):
                for l in range(j):
                    b += farm[k][l]
            for k in range(N):
                for l in range(j, N):
                    c += farm[k][l]
            result.append(max(a, b, c) - min(a, b, c))
    print(f'#{t}', min(result))
            