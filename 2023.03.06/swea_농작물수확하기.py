# SW Expert Academy - 11014 농작물수확하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nongjang = [list(map(int, input().split())) for _ in range(N)]
    min_val = 10000
    for i in range(1, N):
        for j in range(1, N):
            a = 0
            b = 0
            c = 0
            for k in range(i):
                for l in range(j):
                    a += nongjang[k][l]
            for k in range(i, N):
                for l in range(j):
                    b += nongjang[k][l]
            for k in range(N):
                for l in range(j, N):
                    c += nongjang[k][l]
            if min_val > max(a, b, c) - min(a, b, c):
                min_val = max(a, b, c) - min(a, b, c)
    print(f'#{t}', min_val)
