# SW Expert Academy 0227_Start - 12918 start_이진수_확인용

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, num = input().split()
    N = int(N)
    num = int(num, 16)
    print(f'#{t}', bin(num)[2:].zfill(N*4))
    