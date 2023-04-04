# SW Expert Academy 0227_Start - 12919 start_이진수_확인용2

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    num = float(input())
    n = -1
    result = ''
    while num != 0:
        N = 2 ** n
        if num >= N:
            num -= N
            n -= 1
            result += '1'
        else:
            n -= 1
            result += '0'
    if len(result) > 12:
        result = 'overflow'
    print(f'#{t}', result)