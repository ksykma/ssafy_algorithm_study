# SW Expert Academy 0404_그래프 - 11901 그래프_최소 비용

import sys
sys.stdin = open('input.txt', 'r')
            
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    D = [[0xfffff]*N for _ in range(N)]  # cnt 카운트 하는 배열
    D[0][0] = 0
    Q = [(0, 0)]  # 이동 확인
    while Q:
        r, c = Q.pop(0)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                cnt = D[r][c]
                if H[r][c] < H[nr][nc]:
                    cnt += 1 + (H[nr][nc]-H[r][c])
                else:
                    cnt += 1
                if cnt < D[nr][nc]:
                    D[nr][nc] = cnt
                    Q.append((nr, nc))
    print(f'#{t}', D[N-1][N-1])