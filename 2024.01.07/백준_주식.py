# 백준 11501 주식

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for t in range(N):
    n = int(input())
    lst = list(map(int, input().split()))

    answer = 0

    max_val = 0 # 주식 최대값
    for i in range(len(lst)-1, -1, -1):
        if lst[i] > max_val:
            max_val = lst[i]
        else: # 현재 가격이 최대 가격보다 작으면 돈번다.
            answer += max_val - lst[i]

    print(answer)