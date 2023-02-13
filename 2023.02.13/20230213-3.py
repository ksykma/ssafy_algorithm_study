# SW Expert Academy 0206_List02 - 12388

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0]*10 for _ in range(10)]
    for i in nums:
        for j in range(i[1], i[3]+1):
            for k in range(i[0], i[2]+1):
                arr[j][k] += 1
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] > 1:
                cnt += 1
    print(f'#{t}', cnt)