# 백준 2999 비밀 이메일

import sys
sys.stdin = open('input.txt', 'r')

message = input()
N = len(message)
lst = []
for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)
word = ''
n = 0
if len(lst) % 2 == 1:
    R = len(lst) // 2
    M = lst[R]
    while n != M:
        for i in range(n, N, M):
            word += message[i]
        n += 1
else:
    R = len(lst) // 2 - 1
    M = lst[R]
    while n != M:
        for i in range(n, N, M):
            word += message[i]
        n += 1
print(word)
