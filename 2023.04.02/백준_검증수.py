# 백준 2475 검증수

import sys
sys.stdin = open('input.txt', 'r')

lst = list(map(int, input().split()))
result = 0
for i in lst:
    result += i ** 2
print(result%10)