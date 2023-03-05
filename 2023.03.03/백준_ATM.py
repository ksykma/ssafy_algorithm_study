# 백준 11399 ATM

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = sorted(list(map(int, input().split())))
result = 0
cnt = 0
for i in range(N):
    result += cnt + lst[i]
    cnt += lst[i]
print(result)
