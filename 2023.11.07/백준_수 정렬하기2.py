# 백준 2751 수 정렬하기 2

import sys
sys.stdin = open('input.txt', 'r')

import sys
input=sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

for i in sorted(lst):
    print(i)