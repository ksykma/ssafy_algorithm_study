# sw아카데미 Min_Max

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    min_val = 1000000 * N
    max_val = 0
    for i in lst:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    print(f"#{t} {max_val-min_val}")