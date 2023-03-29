# 백준 13300 방 배정

import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.insert(0, [-1, -1])
lst.sort(key=lambda x:x[1])
cnt = 0
plus = 1
f = 0
m = 0
for n in range(1, N+1):
    gender = lst[n][0]
    grade = lst[n][1]
    bigyo = lst[n-1][1]
    if grade == bigyo:
        if gender == 1:
            if m == K:
                cnt += 1
                m = 0
                m += 1
            else:
                m += 1
        else:
            if f == K:
                cnt += 1
                f = 0
                f += 1
            else:
                f += 1
    else:
        if n != 1:
            if f != 0:
                cnt += 1
            if m != 0:
                cnt += 1
            f = 0
            m = 0
            if gender == 1:
                m += 1
            else:
                f += 1
        else:
            if gender == 1:
                m += 1
            else:
                f += 1
if f != 0:
    cnt += 1
if m != 0:
    cnt += 1
print(cnt)
        


