# SW Expert Academy 0227_Start - 12918

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, word = input().split()
    result = ''
    for i in word:
        a = int(i, 16)   # 10진수로
        b = bin(a)[2:]   # 2진수로
        c = b.zfill(4)
        result += c
    print(f'#{t}', result)