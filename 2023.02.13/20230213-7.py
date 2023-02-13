# SW Expert Academy 0213_Stack1 - 2005

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[1] * N for _ in range(1, N + 1)]
    # if N >= 3:
    #     for i in range(N):
    #         if i >= 2:
    #             arr[i]
        
    print(f'#{t}')
    for line in arr:
        print(*line)