# 백준 2720 세탁소 사장 동혁

import sys
sys.stdin = open('input.txt', 'r')

coin = [25, 10, 5, 1]
N = int(input())
pay = [int(input()) for _ in range(N)]

for i in range(N):
    ans = 0
    cnt = 0
    result= [0, 0, 0, 0]
    while ans != pay[i]:
        if ans < pay[i]:
            ans += coin[cnt]
            result[cnt] += 1
        elif ans > pay[i]:
            ans -= coin[cnt]
            result[cnt] -= 1
            cnt += 1
        else:
            break
    print(*result)