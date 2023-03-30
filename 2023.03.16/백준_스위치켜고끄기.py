# 백준 1244 스위치 켜고 끄기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
switch = list(input().split())
S = int(input())
switch.insert(0, '-1')
s = 0
e = 0

for i in range(S):
    gender, num = list(map(int, input().split()))
    if gender == 1:
        for i in range(num, N+1, num):
            if switch[i] == '0':
                switch[i] = '1'
            else:
                switch[i] = '0'
    else:
        n = min(num, N-num+1)
        for i in range(n):
            if switch[num-i] == switch[num+i]:
                s = num-i
                e = num+i
            else:
                break
        for i in range(s, e+1):
            if switch[i] == '0':
                switch[i] = '1'
            else:
                switch[i] = '0'

for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()

    