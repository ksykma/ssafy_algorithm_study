# SW Expert Academy 0201_List01 - 12387

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    a = 0
    max_val = 0
    min_val = 10000 * N
    while a <= N - M:
        num_sum = 0
        for i in range(a, M + a):
            num_sum += nums[i]
        if num_sum > max_val:
            max_val = num_sum
        if num_sum < min_val:
            min_val = num_sum
        num_sum = 0
        a += 1
    print(f'#{t}', max_val - min_val)