# SW Expert Academy 2차배열순회 - 16244

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    arr = [[0]*10 for _ in range(10)]
    for k in range(nums[2]):
        for l in range(nums[2]):
            arr[nums[0]+k][nums[1]+l] += 1
    # for i in range(nums[2]-2):
    #     for j in range(nums[2]-2):
    #         arr[nums[0]+1+i][nums[1]+1+j] -= 1

    print(f'#{t}')
    for line in arr:
        print(*line)