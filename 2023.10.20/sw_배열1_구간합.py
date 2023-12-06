# sw아카데미 구간합

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    min_val = 10000 * M
    max_val = 0
    for i in range(N - M + 1):
        re = 0
        for j in range(i, i + M):
            re += num[j]
        if re < min_val:
            min_val = re
        if re > max_val:
            max_val = re
    print(f"#{t} {max_val - min_val}")