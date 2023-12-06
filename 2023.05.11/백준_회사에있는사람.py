# 백준 2231 분해합

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))
    num_sum = i + num
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)