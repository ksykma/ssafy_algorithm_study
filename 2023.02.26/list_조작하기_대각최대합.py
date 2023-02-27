# SW Expert Academy List(Array)_조작하기 - 11010    

import sys
sys.stdin = open('input.txt', 'r')

def function(r, c):
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]
    num_sum = 0
    for i in range(4):
        for j in range(N):
            nr = r + dr[i] * j
            nc = c + dc[i] * j
            if 0 <= nr < N and 0 <= nc < N:
                num_sum += arr[nr][nc]
    num_sum -= (arr[r][c])*3
    return num_sum

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            result.append(function(i, j))
    print(f'#{t}', max(result))
