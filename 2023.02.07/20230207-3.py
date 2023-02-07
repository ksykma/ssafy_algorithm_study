# SW Expert Academy 2차배열순회 - 16242

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    arr = [[0]*10 for _ in range(10)]
    cnt = 0
    for j in range(nums[3]):
        for k in range(nums[2]):
            cnt += 1
            arr[nums[0]+j][nums[1]+k+(nums[2]-1-2*k)*(j%2)] += cnt
    print(f'#{t}')
    for line in arr:
        print(*line)