# 백준 2292 벌집

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnt = 1
num = 6
room = 1

if N==1:
    print(1)
else:
    while True:
        cnt += num
        room += 1
        if N <= cnt:
            print(room)
            break
        num += 6
