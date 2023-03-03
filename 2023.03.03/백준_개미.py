# 백준 10158 개미

import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())  
p, q = map(int, input().split()) # 초기위치
t = int(input()) # 움직일 시간

# 가로 = [0, 1, 2, 3, 4, 5, 6]
# 세로 = [0, 1, 2, 3, 4]

x = (p+t) // w  # 가로 이동
y = (p+t) // h  # 세로 이동

if x 
result1 = (p+t) % w
result2 = (q+t) % h
















# width = (p+t) // w
# height = (q+t) // h

# if width % 2 == 0:
#     x = (p+t) % w
# else:
#     x = w - (p+t) % w

# if height % 2 == 0:
#     y = (q+t) % h
# else:
#     y = h - (q+t) % h

# print(x, y)