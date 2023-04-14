# 백준 로봇청소기

import sys
sys.stdin = open('input.txt', 'r')

def robot(r, c, d):
    global cnt
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    check = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if room[nr][nc] == 0:
            check += 1
            break
    if check:
        d = (d+3) % 4
        if room[r+dr[d]][c+dc[d]] == 0:
            room[r+dr[d]][c+dc[d]] = -1
            cnt += 1
            Q.append((r+dr[d], c+dc[d], d))
        else:
            Q.append((r, c, d))
    else:
        if room[r-dr[d]][c-dc[d]] != 1:
            Q.append((r-dr[d], c-dc[d], d))
        else:
            return         

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
Q = []
Q.append((r, c, d))
room[r][c] = -1
cnt = 1
while Q:
    r, c, d = Q.pop(0)
    robot(r, c, d)
print(cnt)