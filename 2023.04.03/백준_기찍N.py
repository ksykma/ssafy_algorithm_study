# 백준 2741 N 찍기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for i in range(N, 0, -1):
    print(i)