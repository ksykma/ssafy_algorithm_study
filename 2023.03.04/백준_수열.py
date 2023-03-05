# 백준 2491 수열

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))

max_val = 0
cnt = 1
for i in range(N-1):
    if lst[i] <= lst[i+1]:
        cnt += 1
    else:
        if max_val < cnt:
            max_val = cnt
        cnt = 1
if max_val < cnt:
    max_val = cnt
cnt = 1        
for i in range(N-1):
    if lst[i] >= lst[i+1]:
        cnt += 1
    else:
        if max_val < cnt:
            max_val = cnt
        cnt = 1
if max_val < cnt:
    max_val = cnt
print(max_val)