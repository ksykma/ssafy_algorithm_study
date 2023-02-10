# SW Expert Academy 0210_문제풀이2 - 1946

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [input().split() for _ in range(N)]
    sum_val = ''
    for i in range(N):
        sum_val += lst[i][0] * int(lst[i][1])
    print(f'#{t}')

    cnt = 0
    for idx in range(len(sum_val)):
        print(sum_val[idx], end='')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    print()