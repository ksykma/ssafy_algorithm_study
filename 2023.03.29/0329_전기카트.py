# SW Expert Academy 0327_완탐_탐욕 - 전기카트

import sys
sys.stdin = open('input.txt', 'r')

def func(k, cost):
    global ans
    if ans <= cost:
        return
    if k == N:
        cost += arr[order[k-1]][0]
        if ans > cost:
            ans = cost
    else:
        for i in range(k, N):
            order[k], order[i] = order[i], order[k]
            func(k+1, cost + arr[order[k-1]][order[k]])
            order[k], order[i] = order[i], order[k]
            

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    order = [i for i in range(N)]
    ans = 0xffffffff
    func(1, 0)
    print(f'#{t}', ans)