# 백준 1726 로봇

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(r, c, d):
    global ans

    Q = deque([[r, c, d, 0]])
    visited[r][c][d] = 1
    while Q:
        r, c, d, cnt = Q.popleft()

        if r == r2 - 1 and c == c2 - 1 and d == t2:
            ans = cnt
            return

        for i in range(1, 4):
            nr = r + (dr[d] * i)
            nc = c + (dc[d] * i)
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc][d] == 1:
                continue
            if factory[nr][nc] == 1:
                break
            visited[nr][nc][d] = 1
            Q.append([nr, nc, d, cnt + 1])

        if d == 1 or d == 2:
            if visited[r][c][3] == 0:
                visited[r][c][3] = 1
                Q.append([r, c, 3, cnt + 1])
            if visited[r][c][4] == 0:
                visited[r][c][4] = 1
                Q.append([r, c, 4, cnt + 1])
        else:
            if visited[r][c][1] == 0:
                visited[r][c][1] = 1
                Q.append([r, c, 1, cnt + 1])
            if visited[r][c][2] == 0:
                visited[r][c][2] = 1
                Q.append([r, c, 2, cnt + 1])

N, M = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(N)]
r1, c1, t1 = map(int, input().split())
r2, c2, t2 = map(int, input().split())

# 동 서 남 북 1 2 3 4
dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]

ans = 0
visited = [[[0] * 5 for _ in range(M)] for _ in range(N)]

bfs(r1 - 1, c1 - 1, t1)
print(ans)









# visited = [[0]*M for _ in range(N)]
# # 동0 서1 남2 북3
# direct = [[[2, 3], [1]], [[2, 3], [0]], [[0, 1], [3]], [[0, 1], [2]]] # 동서남북
# dr = [0, 0, 1, -1] # 동서남북
# dc = [1, -1, 0, 0]
# Q = []
# r1 = r1-1
# c1 = c1-1
# t1 = t1-1
# r2 = r2-1
# c2 = c2-1
# t2 = t2-1
# Q.append((r1, c1, t1, 0, 0, 0))
# visited[r1][c1] = 1
# ans = 0xfffff
# tturn = 0
# check = 0
# while Q:
#     r, c, d, go, turn, cnt = Q.pop(0)
#     if r == r2 and c == c2:
#         if ans > go+turn:
#             ans = go+turn
#             tturn = d
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if visited[nr][nc] == 0 and factory[nr][nc] == 0:
#                 if i == d:
#                     if cnt == 0:
#                         visited[nr][nc] = go+turn
#                         Q.append((nr, nc, d, go+1, turn, 1))
#                     else:
#                         if cnt == 3:
#                             visited[nr][nc] = go+turn
#                             Q.append((nr, nc, d, go+1, turn, 1))
#                         else:
#                             visited[nr][nc] = go+turn
#                             Q.append((nr, nc, d, go, turn, cnt+1))
#                 else:
#                     if i in direct[d][0]:
#                         visited[nr][nc] = go+turn
#                         Q.append((nr, nc, i, go+1, turn+1, 1))
#                     else:
#                         visited[nr][nc] = go+turn
#                         Q.append((nr, nc, i, go+1, turn+2, 1))
#             elif visited[nr][nc] != 0 and factory[nr][nc] == 0:
#                 if i == d:
#                     if cnt == 0:
#                         if visited[nr][nc] > go+turn+1:
#                             visited[nr][nc] = go+turn
#                             Q.append((nr, nc, d, go+1, turn, 1))
#                     else:
#                         if cnt == 3:
#                             if visited[nr][nc] > go+turn+1:
#                                 visited[nr][nc] = go+turn
#                                 Q.append((nr, nc, d, go+1, turn, 1))
#                         else:
#                             if visited[nr][nc] > go+turn:
#                                 visited[nr][nc] = go+turn
#                                 Q.append((nr, nc, d, go, turn, cnt+1))
#                 else:
#                     if i in direct[d][0]:
#                         if visited[nr][nc] > go+turn+2:
#                             visited[nr][nc] = go+turn
#                             Q.append((nr, nc, i, go+1, turn+1, 1))
#                     else:
#                         if visited[nr][nc] > go+turn+3:
#                             visited[nr][nc] = go+turn
#                             Q.append((nr, nc, i, go+1, turn+2, 1))


# if tturn != t2:
#     if t2 in direct[tturn][0]:
#         print(ans+1)
#     else:
#         print(ans+2)
# else:
#     print(ans)

# 값이 더 큰에 먼저 같은 경로에 도착하면 어케???????? 
    
# # 백준 2479 경로 찾기

# import sys
# sys.stdin = open('input.txt', 'r')

# N, M = map(int, input().split())
# factory = [list(map(int, input().split())) for _ in range(N)]
# r1, c1, t1 = map(int, input().split())
# r2, c2, t2 = map(int, input().split())
# visited = [[0]*M for _ in range(N)]
# # 동0 서1 남2 북3
# direct = [[[2, 3], [1]], [[2, 3], [0]], [[0, 1], [3]], [[0, 1], [2]]] # 동서남북
# dr = [0, 0, 1, -1] # 동서남북
# dc = [1, -1, 0, 0]
# Q = []
# r1 = r1-1
# c1 = c1-1
# t1 = t1-1
# r2 = r2-1
# c2 = c2-1
# t2 = t2-1
# Q.append((r1, c1, t1, 0, 0, 0))
# visited[r1][c1] = 1
# ans = 0xfffff
# tturn = 0
# while Q:
#     r, c, d, go, turn, cnt = Q.pop(0)
#     # print(go, turn)
#     if r == r2 and c == c2:
#         if ans > go+turn:
#             ans = go+turn
#             tturn = d
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if factory[nr][nc] == 0:
#                 if i == d:
#                     if cnt == 0:
#                         Q.append((nr, nc, d, go+1, turn, 1))
#                         if visited[nr][nc] == 0:
#                             visited[nr][nc] = go+1+turn
#                         else:
#                             if visited[nr][nc] > go+1+turn:
#                                 visited[nr][nc] = go+1+turn
#                     else:
#                         if cnt == 3:
#                             Q.append((nr, nc, d, go+1, turn, 1))
#                             if visited[nr][nc] == 0:
#                                 visited[nr][nc] = go+1+turn
#                             else:
#                                 if visited[nr][nc] > go+1+turn:
#                                     visited[nr][nc] = go+1+turn
#                         else:
#                             Q.append((nr, nc, d, go, turn, cnt+1))
#                             if visited[nr][nc] == 0:
#                                 visited[nr][nc] = go+turn
#                             else:
#                                 if visited[nr][nc] > go+turn:
#                                     visited[nr][nc] = go+turn
#                 else:
#                     if i in direct[d][0]:
#                         Q.append((nr, nc, i, go+1, turn+1, 1))
#                         if visited[nr][nc] == 0:
#                             visited[nr][nc] = go+turn+2
#                         else:
#                             if visited[nr][nc] > go+turn:
#                                 visited[nr][nc] = go+turn+2
#                     else:
#                         Q.append((nr, nc, i, go+1, turn+2, 1))
#                         if visited[nr][nc] == 0:
#                             visited[nr][nc] = go+turn+3
#                         else:
#                             if visited[nr][nc] > go+turn:
#                                 visited[nr][nc] = go+turn+3

# if tturn != t2:
#     if t2 in direct[tturn][0]:
#         print(visited[r2][c2]+1)
#     else:
#         print(visited[r2][c2]+2)
# else:
#     print(visited[r2][c2])