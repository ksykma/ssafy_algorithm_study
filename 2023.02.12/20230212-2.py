# SW Expert Academy 0203_문제풀이1 - 9386

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(input())
    max_val = 0
    cnt = 0
    for i in lst:
        if int(i) == 1:
            cnt += 1
            if cnt > max_val:
                max_val = cnt
        else:
            cnt = 0
    print(f'#{t} {max_val}')

