# 백준 9086 문자열

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    word = input()
    print(word[0], end='')
    print(word[-1])