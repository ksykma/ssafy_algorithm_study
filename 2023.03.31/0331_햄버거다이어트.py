# SW Expert Academy 0331_문제풀이6 - 5215 햄버거 다이어트

import sys
sys.stdin = open('input.txt', 'r')

def hambergur(n, cal, score):
    global ans
    if cal > L:
        return
    for i in range(N):
        if used[i] == 1:
            continue
        used[i] = 1
        if ans <= score:
            hambergur(n+1, cal+lst[i][1], score+lst[i][0])
            ans = max(ans, score)
        used[i] = 0
T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    used = [0] * N
    hambergur(0, 0, 0)
    print(f'#{t}', ans)