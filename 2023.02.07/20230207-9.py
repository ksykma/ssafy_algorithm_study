# SW Expert Academy 0207_List02 - 1954

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(N)
    arr = [[0]*(N) for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    
    a = 1
    b = 0
    while a <= 9:
        for j in range(b, N):
            arr[b][j] = a
            a += 1
        a -= 1
        for i in range(b, N):
            arr[i][N-1] = a
            a += 1
        a -= 1
        for j in range(N-1, b-1, -1):
            arr[N-1][j] = a
            a += 1
        a -= 1
        for i in range(N-1, b, -1):
            arr[i][b] = a
            a += 1
        b += 1
    for line in arr:
        print(*line)