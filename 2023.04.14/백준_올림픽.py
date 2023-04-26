# 백준 8979 올림픽

import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
medal = [list(map(int, input().split())) + [0] for _ in range(N)]
medal.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

rank = 1
for i in range(N):
    if medal[i][4] == 0:
        medal[i][4] = rank
    for j in range(i+1, N):
        if medal[i][1:4] == medal[j][1:4]:
            if medal[j][4] == 0:
                medal[j][4] = rank
    rank += 1

for i in range(N):
    if medal[i][0] == K:
        print(medal[i][4])
# print(medal)