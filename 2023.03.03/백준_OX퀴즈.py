# 백준 8958 OX퀴즈

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    test = list(input())
    N = len(test)
    n = 0
    for i in range(N):
        if test[i] == 'O':
            n += 1
            test[i] = n
        else:
            n = 0
            test[i] = n
    print(sum(test))