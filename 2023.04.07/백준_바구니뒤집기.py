# 백준 5597 과제 안 내신 분..?

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
lst = [i for i in range(1, N+1)]
for m in range(M):
    i, j = map(int, input().split())
    for k in range(len(lst[i-1:j])//2):
        lst[i-1+k], lst[j-1-k] = lst[j-1-k], lst[i-1+k]
print(*lst)