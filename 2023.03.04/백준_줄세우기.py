# 백준 2605 줄 세우기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))
# 13524 42531
result = [1]
n = 2
for i in range(1, N):
    result.insert(lst[i], n)
    n += 1
for i in range(N-1, -1, -1):
    print(result[i], end = ' ')