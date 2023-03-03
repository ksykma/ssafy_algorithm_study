# 백준 8320 직사각형을 만드는 방법

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
cnt = 0
if n % 2 == 0:
    for i in range(1, n // 2 + 1):
        if i == 1:
            cnt += (n // i)
        else:
            square = (n // i)-(i-1)
            if square > 0:
                cnt += square
else:
    for i in range(1, n // 2 + 2):
        if i == 1:
            cnt += (n // i)
        else:
            square = (n // i)-(i-1)
            if square > 0:
                cnt += square
print(cnt)