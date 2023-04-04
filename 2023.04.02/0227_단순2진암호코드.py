# SW Expert Academy 0227_Start - 1240 단순 2진 암호코드

import sys
sys.stdin = open('input.txt', 'r')

dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in range(N):
        if '1' in arr[i]:
            secret = arr[i].rstrip('0')[-56:]
            break
    lst = []
    for i in range(8):
        lst.insert(0, dict.get(secret[-7:]))
        secret = secret[:-7]
    odd = 0
    even = 0
    for i in range(8):
        if i % 2 == 0:
            odd += lst[i]
        else:
            even += lst[i]
    if (odd*3 + even) % 10 == 0:
        print(f'#{t}', odd+even)
    else:
        print(f'#{t}', 0)