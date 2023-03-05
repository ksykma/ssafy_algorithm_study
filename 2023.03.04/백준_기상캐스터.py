# 백준 10709 기상캐스터

import sys
sys.stdin = open('input.txt', 'r')

H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]
result = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        n = 1
        for k in range(1, W):
            if sky[i][j] == 'c':
                result[i][j] = 0
                nr = i
                nc = j + 1*k
                if 0 <= nc < W:
                    result[nr][nc] = n
                    n += 1
        n = 1
for line in result:
    print(*line)