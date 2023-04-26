# 백준 2146 다리 만들기

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
check = [[0]*N for _ in range(N)]
Q = deque()
cnt = 2
for i in range(N):
    for j in range(N):
        if island[i][j] == 1 and check[i][j] == 0:
            Q.append((i, j))
            check[i][j] = cnt
            while Q:
                r, c = Q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if island[nr][nc] == 1 and check[nr][nc] == 0:
                            check[nr][nc] = cnt
                            Q.append((nr, nc))
            cnt += 1
min_val = 0xfffff
for i in range(N):
    for j in range(N):
        if check[i][j] != 0:
            Q = deque()
            end = 0
            Q.append((i, j))
            visited = [[0]*N for _ in range(N)]
            while Q:
                r, c = Q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if check[nr][nc] == 0 and visited[nr][nc] == 0:
                            visited[nr][nc] = visited[r][c] + 1
                            Q.append((nr, nc))
                        if check[nr][nc] != 0 and check[nr][nc] != check[i][j]:
                            if min_val > visited[r][c]:
                                min_val = visited[r][c]
                            end = 1
                            break
                if end == 1:
                    break
print(min_val)



# lst = []
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni = i + dr[k]
#             nj = j + dc[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 if island[i][j] == 1 and island[ni][nj] == 0:
#                     lst.append((i, j))
#                     break
# min_val = 0xfffff
# for i in range(len(lst)):
#     Q = deque()
#     Q.append(lst[i])
#     visited = [[0]*N for _ in range(N)]
#     visited[lst[i][0]][lst[i][1]] = 1
#     check = 0
#     while Q:
#         r, c = Q.popleft()
#         if visited[r][c] > min_val:
#             break
#         for j in range(4):
#             nr = r + dr[j]
#             nc = c + dc[j]
#             if 0 <= nr < N and 0 <= nc < N:
#                 if island[nr][nc] == 0 and visited[nr][nc] == 0:
#                     visited[nr][nc] = visited[r][c] + 1
#                     Q.append((nr, nc))
#                 if island[nr][nc] == 1:
#                     if min_val > visited[r][c]:
#                         min_val = visited[r][c]
#                         check = 1
#                     break
#         if check == 1:
#             break
# print(min_val)
