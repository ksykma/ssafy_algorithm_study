# 백준 10814 나이순 정렬

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [list(input().split()) for _ in range(N)]
lst.sort(key = lambda x : int(x[0]))

for line in lst:
    print(*line)