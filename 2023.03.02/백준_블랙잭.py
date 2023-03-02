# 백준 2798 블랙잭

import sys
sys.stdin = open('input.txt', 'r')

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))

min_val = 300000
result = 0
sum_num = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_num += lst[i]
            sum_num += lst[j]
            sum_num += lst[k]
            if sum_num <= M:
                if min_val > M - sum_num:
                    min_val = M - sum_num
                    result = sum_num
                    sum_num = 0
                else:
                    sum_num = 0
            else:
                sum_num = 0
    if result == M:
        break
print(result)