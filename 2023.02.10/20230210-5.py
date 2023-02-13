# SW Expert Academy 0210_문제풀이2 - 2001

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    a = 0
    max_val = 0
    b = 0
    while a <= N - M:
        while b <= N - M:
            result = 0
            for i in range(a, M + a):
                for j in range(b, M + b):
                    result += lst[i][j]
            if max_val < result:
                max_val = result
            b += 1
        a += 1
        b = 0

    print(f'#{t} {max_val}')
