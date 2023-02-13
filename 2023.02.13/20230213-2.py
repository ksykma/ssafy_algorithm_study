# SW Expert Academy 0206_List02 - 1209

import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0
    for i in range(100):
        w = 0 # 가로
        h = 0 # 세로
        for j in range(100):
            w += arr[i][j]
            h += arr[j][i]
        if max_val < w:
            max_val = w
        if max_val < h:
            max_val = h
    d = 0  # 대각선
    for i in range(100):
        d += arr[i][i]
    if max_val < d:
        max_val = d
    u = 0
    for i in range(100):
        u += arr[i][99 - i]
    if max_val < u:
        max_val = u
    print(f'#{tc}', max_val)


