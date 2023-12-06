# 백준 2751 수 정렬하기 3

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
print(lst)
for i in sorted(lst):
    print(i)
