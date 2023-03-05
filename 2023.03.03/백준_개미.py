# 백준 10158 개미

import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split()) # 6 4
p, q = map(int, input().split()) # 4 1 5 3
t = int(input()) # 움직일 시간 8 4

# 가로 = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]
# 세로 = [0, 1, 2, 3, 4, 3, 2, 1, 0]


x = (p+t) // w  # 가로 이동 12 // 6 9 // 6
y = (q+t) // h  # 세로 이동 9 // 4 7 // 4

if x % 2 == 0:
    result1 = (p+t) % w
else:
    result1 = w - (p+t) % w

if y % 2 == 0:
    result2 = (q+t) % h
else:
    result2 = h - (q+t) % h

print(result1, result2)