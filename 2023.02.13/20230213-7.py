# SW Expert Academy 0213_Stack1 - 2005

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[1] * i for i in range(1, N + 1)]
    for k in range(N):
        if k >= 2:
            for j in range(1, k-1):
                for l in range(k-2):
                    arr[k][j] = arr[k-1][l] + arr[k-1][l+1]

    print(f'#{t}')
    for line in arr:
        print(*line)