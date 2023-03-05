# 백준 2567 색종이-2

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [[0]*100 for _ in range(100)]
for i in range(N):
    color = list(map(int, input().split()))
    r = color[1]
    c = color[0]
    for i in range(c, c+10):
        for j in range(r, r+10):
            arr[i][j] = 1
def function(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 100 and 0 <= nc < 100:
            if arr[nr][nc] == 1:
                cnt += 1
    return cnt

result = 0   
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            a = function(i, j)
            if a == 3:
                result += 1
            elif a == 2:
                result += 2
print(result)