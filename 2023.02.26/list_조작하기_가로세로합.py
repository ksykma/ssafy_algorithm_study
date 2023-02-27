# SW Expert Academy List(Array)_조작하기 - 10593    

import sys
sys.stdin = open('input.txt', 'r')

def function(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = 0
    for i in range(4):
        for j in range(N):
            nr = r + dr[i] * j
            nc = c + dc[i] * j
            if 0 <= nr < N and 0 <= nc < N:
                result += arr[nr][nc]
    result -= arr[r][c] * 3
    return result
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            ans.append(function(i, j))
    print(f'#{t}', max(ans))