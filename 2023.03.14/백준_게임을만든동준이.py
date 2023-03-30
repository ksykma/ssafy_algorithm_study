# 백준 2847 게임을 만든 동준이

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [int(input()) for _ in range(N)]
result = 0
for i in range(N-1, 0, -1):
    if lst[i] <= lst[i-1]:
        while True:
            lst[i-1] -= 1
            result += 1
            if lst[i] > lst[i-1]:
                break
print(result)