# SW Expert Academy 0220_Queue - 5688

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = 1
    while num*num*num != N:
        if num*num*num > N:
            num = -1
            break
        num += 1
    print(f'#{t}', num)