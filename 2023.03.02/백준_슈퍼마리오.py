# 백준 2851 슈퍼 마리오

import sys
sys.stdin = open('input.txt', 'r')

mushroom = [int(input()) for _ in range(10)]
result = 0
num_sum = 0
min_val = 100
for i in range(10):
    if num_sum <= 100:
        num_sum += mushroom[i]
        if abs(100 - num_sum) <= min_val:
            min_val = abs(100 - num_sum)
            result = num_sum
print(result)