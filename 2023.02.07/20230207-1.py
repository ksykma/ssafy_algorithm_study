# SW Expert Academy 0206_List02 - 11008

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = []
    for n in range(N):
        nums = list(map(int, input().split()))
        lst.append(nums)
    max_val = 0
    max_raw = 0
    max_col = 0
    for i in range(N):
        for j in range(N):
            num_sum = 0
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    num_sum += lst[ni][nj]
            if max_val < num_sum:
                max_val = num_sum
                max_raw = i
                max_col = j
    print(f'#{t} {max_raw} {max_col} {max_val}')
