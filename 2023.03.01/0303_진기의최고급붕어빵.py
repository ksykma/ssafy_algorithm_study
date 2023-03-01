# SW Expert Academy 0303_문제풀이5 - 1860

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    result = 'Possible'
    fish_cnt = max(lst) // M * K
    for i in range(N):
        if lst[i] < M:
            result = 'Impossible'
            break
        else:
            if N > fish_cnt:
                result = 'Impossible'
                break
    print(f'#{t}', result)