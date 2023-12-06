# 백준 23971 ZOAC 4

import sys
sys.stdin = open('input.txt', 'r')

H, W, N, M = map(int, input().split())
room = [[0]*W for _ in range(H)]
room[0][0] = 1

for i in range(H):
    for j in range(W):
        dr = [-1, 1, 0, 0, -1, -1, 1, 1]
        dc = [0, 0, -1, 1, -1, 1, -1, 1]
        cnt = 0
        for k in range(8):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < H and 0 <= nc < W:
                if room[nr][nc] == 1:
                    cnt += 1
        if cnt == 0:
            room[i][j] = 1

result = 0
for i in range(H):
    result += sum(room[i])

print(result)