# SW Expert Academy 0303_문제풀이5 - 1860

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    lst = sorted(list(map(int, input().split())))
    result = 'Possible'
    for i in range(N):
        fish_cnt = (lst[i] // M) * K - (i+1)
        if fish_cnt < 0:
            result = 'Impossible'
            break
    print(f'#{t}', result)