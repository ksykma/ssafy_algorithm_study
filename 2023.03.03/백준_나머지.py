# 백준 3052 나머지

import sys
sys.stdin = open('input.txt', 'r')

lst = []
for i in range(10):
    lst.append(int(input()) % 42)
print(len(set(lst)))
