# sw아카데미 Sum

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0
    for i in range(100):
        cnt = 0
        for j in range(100):
