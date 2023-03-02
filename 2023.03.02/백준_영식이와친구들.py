# 백준 1592 영식이와 친구들

import sys
sys.stdin = open('input.txt', 'r')

N, M, L = list(map(int, input().split()))
# N : 앉는 자리, M : 공을 최대 받는 횟수, L : 공을 전달하는 위치
lst = [0] * N
n = 0
cnt = 0
lst[0] = 1
while True:
    if lst[n] == M:
            break
    if lst[n] % 2 == 1:
        n = (N+n+L)%N
        lst[n] += 1
        cnt += 1
    else:
        n = (N+n-L)%N
        lst[n] += 1
        cnt += 1
print(cnt)
