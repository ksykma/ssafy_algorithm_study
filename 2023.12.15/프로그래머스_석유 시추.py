# from collections import deque

# def solution(land):
#     answer = 0
#     land_r = len(land) # 5
#     land_c = len(land[0]) # 8
#     for j in range(land_c): # 가로
#         visited = [[0 for _ in range(len(land[0]))] for k in range(land_r)]
#         for i in range(land_r): # 세로
#             if land[i][j] == 1:
#                 dr = [-1, 1, 0, 0]
#                 dc = [0, 0, -1, 1]
#                 Q = deque([[i, j]])
#                 visited[i][j] = 1
#                 while Q:
#                     r, c = Q.popleft()
#                     for q in range(4):
#                         nr = r + dr[q]
#                         nc = c + dc[q]
#                         if 0 <= nr < len(land) and 0 <= nc < len(land[0]):
#                             if land[nr][nc] == 1 and visited[nr][nc] == 0:
#                                 visited[nr][nc] = 1
#                                 Q.append([nr, nc])
#         cnt = 0
#         for l in range(len(visited)):
#             cnt += sum(visited[l])
#         if cnt > answer:
#             answer = cnt
#     return answer

from collections import deque

def solution(land):
    answer = 0
    land_r = len(land) # 5
    land_c = len(land[0]) # 8
    visited = [[0 for _ in range(len(land[0]))] for k in range(land_r)]
    for j in range(land_c): # 가로
        for i in range(land_r): # 세로
            if land[i][j] == 1:
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]
                Q = deque([[i, j]])
                visited[i][j] = 1
                while Q:
                    r, c = Q.popleft()
                    for q in range(4):
                        nr = r + dr[q]
                        nc = c + dc[q]
                        if 0 <= nr < len(land) and 0 <= nc < len(land[0]):
                            if land[nr][nc] == 1 and visited[nr][nc] == 0:
                                visited[nr][nc] = visited[r][c] + 1
                                Q.append([nr, nc])
        # cnt = 0
        # for l in range(len(visited)):
        #     cnt += sum(visited[l])
        # if cnt > answer:
        #     answer = cnt
    return visited

print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))