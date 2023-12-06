# 백준 2444 별 찍기 - 7

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))