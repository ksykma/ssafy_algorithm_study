# SW Expert Academy 0221_Queue - 11652

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        if arr[0][i] == '3':
            start = i
    visited = [[0] * N for _ in range(N)]
    visited[0][start] = 1
    