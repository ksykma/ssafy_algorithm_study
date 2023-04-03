# 백준 2577 숫자의 개수

import sys
sys.stdin = open('input.txt', 'r')

A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
for i in range(10):
    print(result.count(str(i)))