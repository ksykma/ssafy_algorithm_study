# SW Expert Academy 0203_문제풀이1 - 9367

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 0
    max_val = 0
    for i in range(N-1):
        if C[i+1] > C[i]:
            cnt += 1
            if cnt > max_val:
                max_val = cnt
        else:
            cnt = 0
    print(f'#{t}', max_val + 1)