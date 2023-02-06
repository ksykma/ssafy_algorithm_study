# SW Expert Academy 0206_List02 - 12388

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = []
    for n in range(N):
        nums = list(map(int, input().split()))
        lst.append(nums)
    arr = [[0]*10 for _ in range(10)]
    for i in lst:
        for r in range(i[1], i[3]+1):
            for c in range(i[0], i[2]+1):
                arr[r][c] += 1
    count = 0
    for a in range(10):
        for b in range(10):
            if arr[a][b] > 1:
                count += 1
    print(f'#{t} {count}')
        
