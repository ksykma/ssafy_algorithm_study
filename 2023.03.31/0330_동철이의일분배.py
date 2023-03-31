# SW Expert Academy 0330_분할_백트래킹 - 1865 동철이의 일 분배

import sys
sys.stdin = open('input.txt', 'r')

def dongcheol(k, cost):
    global ans
    if k == N:
        if ans < cost:
            ans = cost
    else:
        for i in range(N):
            if used[i] == 1:
                continue
            used[i] = 1
            if ans < cost * (n_lst[k][cors[i]]/100):
                dongcheol(k+1, cost * (n_lst[k][cors[i]]/100))
            used[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    n_lst = [list(map(int, input().split())) for _ in range(N)]
    cors = [i for i in range(N)]
    used = [0] * N
    ans = 0
    dongcheol(0, 1)
    print(f'#{t}', "{:.6f}".format(ans*100))