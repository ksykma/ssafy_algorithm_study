# SW Expert Academy 0206_List02 - 12388    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for i in range(N):
        nums = list(map(int, input().split()))
        for j in range(nums[0], nums[2]+1):
            for k in range(nums[1], nums[3]+1):
                arr[j][k] += 1
    result = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                result += 1
    print(f'#{t}', result)