# SW Expert Academy 2차배열순회 - 16240

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    arr = [[0]*10 for _ in range(10)]
    for i in range(nums[2]):
        arr[nums[0]+i][nums[1]+i] = 1
        arr[nums[0]+i][nums[1]+nums[2]-1-i] = 1



    print(f'#{t}')
    for line in arr:
        print(*line)
