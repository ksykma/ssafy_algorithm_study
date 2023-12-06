# 백준 11650 좌표 정렬하기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[0], x[1]))
for i in lst:
    print(*i)