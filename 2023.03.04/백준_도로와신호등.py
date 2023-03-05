# 백준 2980 도로와 신호등

import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
truck = 0
time = 0
for i in range(N):
    D, R, G = list(map(int, input().split()))
    # D는 신호등의 위치, R는 빨강 G는 초록
    for j in range(L):
        truck += 1
        if truck == D:
            if truck < R+G:
                time += R - truck
            else:
                if D % (R+G) < R:
                    time += D % (R+G)
        if truck
print(L+time)