# 백준 1920 수 찾기

import sys
sys.stdin = open('input.txt', 'r')

import sys

N = int(sys.stdin.readline())
lst1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

for i in lst2:
    if i in lst1:
        print(1)
    else:
        print(0)