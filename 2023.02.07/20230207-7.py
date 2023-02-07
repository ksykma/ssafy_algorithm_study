# SW Expert Academy 2차배열순회 - 1210

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    n = 0
    while n <= 2:
        for i in range(100):
            for j in range(100):
                if arr[0][j] == 1:
                    while arr[i][j+1] == 1 or arr[i][j-1] == 1:
                        i += 1
                    
                    