# 백준 2559 수열

import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
temp = list(map(int, input().split()))
n = 0
max_val = -100 * K
first = sum(temp[0:K])
for i in range(N-K):
    if max_val < first:
        max_val = first
    first = first - temp[i] + temp[K+i]
if max_val < first:
    max_val = first
print(max_val)
    


