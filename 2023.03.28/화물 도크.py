# SW Expert Academy 0328_완탐_탐욕 - 화물 도크

import sys
sys.stdin = open('input.txt', 'r')

def function(n):
    global cnt, m, r
    if r == N-1:
        return
    for i in range(r, N):
        r = i
        if lst[i][0] >= n:
            cnt += 1
            m = lst[i][1]
            break
    function(m)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x:x[1])
    cnt = 1
    r = 1
    m = lst[0][1]
    function(m)
    print(f'#{t}', cnt)