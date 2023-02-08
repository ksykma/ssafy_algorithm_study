# SW Expert Academy 0208_String - 12395

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_val = 0
    cnt = 0
    for i in str1:
        for j in str2:
            if i == j:
                cnt += 1
        if max_val < cnt:
            max_val = cnt
        cnt = 0
    print(f'#{t} {max_val}')