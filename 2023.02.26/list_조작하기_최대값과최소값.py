# SW Expert Academy List(Array)_조작하기 - 11084    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_val = 0
    max_idx = 0
    min_val = 100
    min_idx = 0
    for i in range(N):
        if lst[i] >= max_val:
            max_val = lst[i]
            max_idx = i
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
    print(f'#{t}', abs(max_idx-min_idx))