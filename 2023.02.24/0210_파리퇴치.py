# SW Expert Academy 0210_문제풀이2 - 2001    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for l in range(N - M + 1):
        for i in range(N - M + 1):
            num = 0
            for j in range(M):
                for k in range(M):
                    num += arr[j+l][k+i]
            if max_val < num:
                max_val = num
    print(f'#{t}', max_val)