# 백준 2116 주사위 쌓기

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

lst = [dice[0][0], dice[0][1], dice[0][2], dice[0][3], dice[0][4], dice[0][5]]
max_val = 0
cnt = 0
for k in range(6):
    change = lst[k]
    for i in range(N):
        for j in range(6):
            if dice[i][j] == change:
                if j == 0:
                    change = dice[i][5]
                    cnt += max(dice[i][1], dice[i][2], dice[i][3] ,dice[i][4])
                elif j == 1:
                    change = dice[i][3]
                    cnt += max(dice[i][0], dice[i][2], dice[i][4] ,dice[i][5])
                elif j == 2:
                    change = dice[i][4]
                    cnt += max(dice[i][0], dice[i][1], dice[i][3] ,dice[i][5])
                elif j == 3:
                    change = dice[i][1]
                    cnt += max(dice[i][0], dice[i][2], dice[i][4] ,dice[i][5])
                elif j == 4:
                    change = dice[i][2]
                    cnt += max(dice[i][0], dice[i][1], dice[i][3] ,dice[i][5])
                elif j == 5:
                    change = dice[i][0]
                    cnt += max(dice[i][1], dice[i][2], dice[i][3] ,dice[i][4])
                break

    if cnt > max_val:
        max_val = cnt
    
    cnt = 0

print(max_val)