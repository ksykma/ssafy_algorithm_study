# SW Expert Academy 0227_Start - 완전검색_최소합

import sys
sys.stdin = open('input.txt', 'r')

def function(r, c):
    dr = [1, 0]
    dc = [0, 1]
    lst = []
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            lst.append(arr[nr][nc])
    if len(lst) == 2:
        if lst[0] == lst[1]:
            pass
        else:
            min(lst)
    

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r = 0
    c = 0
    while r != N-1 and c != N-1:
        function(r, c)
    