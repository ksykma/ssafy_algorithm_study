# 백준 1292 쉽게 푸는 문제

import sys
sys.stdin = open('input.txt', 'r')

s, e = list(map(int, input().split()))

result = 0
N = 0
num = 1
while N != e:
    if (e - N) >= num:
        result += num * num
        N += num
        num += 1
    else:
        result += num * (e - N)
        N += e - N

N = 0
num = 1
while N != s-1:
    if (s - 1 - N) >= num:
        result -= num * num
        N += num
        num += 1
    else:
        result -= num * (s - 1 - N)
        N += s - 1 - N
print(result)