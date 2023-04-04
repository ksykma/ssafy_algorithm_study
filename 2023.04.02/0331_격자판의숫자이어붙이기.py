# SW Expert Academy 230331: 문제풀이_6 - 14035 격자판의 숫자 이어 붙이기

import sys
sys.stdin = open('input.txt', 'r')

# def move(n, r, c, result):
#     global lst
#     if n == 6:
#         lst[n].add(result)
#         return
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < 4 and 0 <= nc < 4:
#             plus = result+arr[nr][nc]
#             lst[n].add(plus)
#             move(n+1, nr, nc, plus)
# T = int(input())
# for t in range(1, T + 1):
#     arr = [list(input().split()) for _ in range(4)]
#     lst = [set() for _ in range(7)]
#     for i in range(4):
#         for j in range(4):
#             lst[0].add(arr[i][j])
#             move(0, i, j, arr[i][j])
#     print(f'#{t}', len(lst))


def move(n, r, c, result):
    global lst
    if n == 6:
        if result not in lst:
            lst.append(result)
        return
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            move(n+1, nr, nc, result+arr[nr][nc])
T = int(input())
for t in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    lst = []
    for i in range(4):
        for j in range(4):
            s = arr[i][j]
            move(0, i, j, s)
    print(f'#{t}', len(lst))