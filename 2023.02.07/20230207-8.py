# SW Expert Academy 0207_List02 - 1966

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N-1):
        min_val = i
        for j in range(i + 1, N):
            if nums[min_val] > nums[j]:
                min_val = j
        nums[i], nums[min_val] = nums[min_val], nums[i]
    print(f'#{t}', *nums)