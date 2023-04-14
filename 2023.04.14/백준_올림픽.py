# 백준 8979 올림픽

import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
medal = [list(map(int, input().split())) + [0] for _ in range(N)]
for i in range(N-1):
    if medal[i][1] <= medal[i+1][1]:
        medal[i], medal[i+1] = medal[i+1], medal[i]
for i in range(N-1):
    if medal[i][2] <= medal[i+1][2]:
        if medal[i][1] > medal[i+1][1]:
            continue
        medal[i], medal[i+1] = medal[i+1], medal[i]
for i in range(N-1):
    if medal[i][3] <= medal[i+1][3]:
        if medal[i][1] > medal[i+1][1]:
            continue
        if medal[i][2] > medal[i+1][2]:
            continue
        medal[i], medal[i+1] = medal[i+1], medal[i]

rank = 1
for i in range(N-1):
    if (medal[i][1], medal[i][2], medal[i][3]) == (medal[i+1][1], medal[i+1][2], medal[i+1][3]):
        medal[i][4] = rank
        medal[i+1][4] = rank
        rank += 1
    else:
        if medal[i][4] == 0:
            medal[i][4] = rank
            rank += 1
        else:
            rank += 1
if medal[-1][4] == 0:
    medal[-1][4] = rank            

for i in range(N):
    if medal[i][0] == K:
        print(medal[i][4])