# 백준 10157 자리배정

import sys
sys.stdin = open('input.txt', 'r')

def function(r, c):
    n = 1
    a = 1
    b = 1
    arr[R-1][0] = 1
    dr = [-1, 0, 1, 0] # 상우하좌
    dc = [0, 1, 0, -1]
    while n != K:
        for i in range(4):
            if i % 2 == 1:
                N = C
            else:
                N = R
            for j in range(1, N):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] != 0:
                        nr -= dr[i]
                        nc -= dc[i]
                        break
                    else:
                        n += 1
                        if i == 0:
                            a += 1
                        elif i == 1:
                            b += 1
                        elif i == 2:
                            a -= 1
                        else:
                            b -= 1
                        arr[nr][nc] = n
                if n == K:
                    break
            if n == K:
                break
            r = nr
            c = nc
    return b, a


C, R = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]

if C*R >= K:
    print(*function(R-1, 0))
else:
    print(0)


        