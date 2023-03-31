# SW Expert Academy 0330_분할_백트래킹 - 11897 최소 생산 비용

import sys
sys.stdin = open('input.txt', 'r')

def cost(k, pay):
    global ans
    if pay > ans:
        return
    if k == N:
        if ans > pay:
            ans = pay
        return
    else:
        for i in range(N):
            if used[i] == 1:
                continue
            used[i] = 1
            cost(k+1, pay + arr[k][idx_lst[i]])
            used[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx_lst = [i for i in range(N)]
    used = [0] * N
    ans = 0xffffffff
    cost(0, 0)
    print(f'#{t}', ans)