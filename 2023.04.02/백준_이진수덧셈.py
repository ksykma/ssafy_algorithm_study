# 백준 1252 이진수 덧셈

import sys
sys.stdin = open('input.txt', 'r')

a, b = map(int, input().split())
print(a, b)
a = int(a, 2)
b = int(b, 2)
# print(bin(a+b))