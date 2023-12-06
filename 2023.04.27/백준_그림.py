# 백준 1926 그림

import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
Q = []
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if painting[i][j] == 1 and check[i][j] == 0:
            Q.append((i, j))
            check[i][j] = 1
            max_val = 1
            while Q:
                r, c = Q.pop(0)
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < m:
                        if check[nr][nc] == 0 and painting[nr][nc] == 1:
                            check[nr][nc] = 1
                            max_val += 1
                            Q.append((nr, nc))
            cnt += 1
            if ans < max_val:
                ans = max_val

print(cnt)
print(ans)
