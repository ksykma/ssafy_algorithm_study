# SW Expert Academy 0227_Start - 12919

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = float(input())
    result = ''
    n = -1
    while N != 0:
        num = 2 ** n
        if N >= num:
            N -= num
            n -= 1
            result += '1'
        else:
            n -= 1
            result += '0'
    if len(result) > 12:
        result = 'overflow'
    print(f'#{t}', result)