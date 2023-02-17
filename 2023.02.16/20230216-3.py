# SW Expert Academy 0215_Stack2 - 11620 

import sys
sys.stdin = open('input.txt', 'r')

def DFS(r, c):
    dr = [-1, 1, 0, 0]   # 상하좌우
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if miro[nr][nc] == 0:
            miro[nr][nc] = 1
            if DFS(nr, nc) == 1:
                return 1
        elif miro[nr][nc] == 3:
            return 1
    return 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    miro = [[1]*(N+2)]+[[1]+list(map(int, input()))+[1] for _ in range(N)]+[[1]*(N+2)]
    for h in range(1, N + 1):
        for w in range(1, N + 1):
            if miro[h][w] == 2:
                goal = miro[h][w]
                print(f'#{t}', DFS(h, w))












