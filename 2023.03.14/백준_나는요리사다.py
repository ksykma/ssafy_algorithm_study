# 백준 2953 나는 요리사다

import sys
sys.stdin = open('input.txt', 'r')

max_val = 0
max_idx = 0
for i in range(5):
    lst = list(map(int, input().split()))
    result = sum(lst)
    if result > max_val:
        max_val = result
        max_idx = i+1
print(max_idx, max_val)