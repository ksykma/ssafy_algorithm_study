# SW Expert Academy 0227_Start - 2805

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    a = -1
    b = N + 1
    num1 = (N // 2) + 1
    num2 = (N // 2) - 1
    result = 0
    while num1 != 0:
        a += 1
        b -= 1
        num1 -= 1
        num2 += 1
        for i in range(a, b):
            result += farm[num1][i]
        for i in range(a, b):
            result += farm[num2][i]
    result -= sum(farm[N//2])
    print(f'#{t}', result)
        
        
            