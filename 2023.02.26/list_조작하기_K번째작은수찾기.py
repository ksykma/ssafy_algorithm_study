# SW Expert Academy List(Array)_조작하기 - 10988    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    # lst = sorted(list(set(map(int, input().split()))))
    # print(f'#{t}', lst[K-1])
    lst = list((map(int, input().split())))
    lst.sort()
    s = 0
    max_val = 0
    for i in range(N):
        if max_val < lst[i]:
            max_val = lst[i]
            s += 1
        if s == K:
            break
    print(f'#{t}', max_val)
            