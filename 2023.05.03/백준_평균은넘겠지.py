# 백준 2479 경로 찾기

import sys
sys.stdin = open('input.txt', 'r')

C = int(input())
for t in range(C):
    score = list(map(int, input().split()))
    N = score[0]
    average = (sum(score)-N) / N
    cnt = 0
    for i in range(1, N+1):
        if score[i] > average:
            cnt += 1
    print("{:.3f}%".format(cnt/N * 100))
    