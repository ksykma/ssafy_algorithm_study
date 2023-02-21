# SW Expert Academy 0207_List02 - 10760

import sys
sys.stdin = open('input.txt', 'r')
def function(r, c):
    dr = [0, 1, 0, -1]   # 우하좌상
    dc = [1, 0, -1, 0]
    arr[0][0] = 1
    a = 1
    while a != N*N:
        for i in range(4):
            for j in range(1, N):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                elif arr[nr][nc] != 0:
                    nr -= dr[i]
                    nc -= dc[i]
                    break
                else:
                    a += 1
                    arr[nr][nc] = a
            r = nr
            c = nc
    return arr

            
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [i for i in range(1, (N*N)+1)]
    arr = [[0]*N for _ in range(N)]
    print(f'#{t}')
    for line in function(0, 0):
        print(*line)