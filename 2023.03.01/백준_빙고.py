# 백준 2578 빙고

import sys
sys.stdin = open('input.txt', 'r')

# me = [list(map(int, input().split())) for _ in range(5)]
# bingo = [list(map(int, input().split())) for _ in range(5)]
# lst = []
# for i in range(5):
#     for j in range(5):
#         lst.append(bingo[i][j])
# O = [0, 0, 0, 0, 0]
# cnt = 0
# result = 12
# k = 0
# check = 0
# while k != 12:
#     for i in range(5):
#         for j in range(5):
#             if me[i][j] == lst[k]:
#                 me[i][j] = 0
#                 k += 1
#                 check = 1
#                 break
#         if check == 1:
#             check = 0
#             break
# while cnt != 3:
#     for i in range(5):
#         for j in range(5):
#             if me[i][j] == lst[k]:
#                 me[i][j] = 0
#                 result += 1
#                 check = 1
#                 break
#         if check == 1:
#             check = 0
#             break
#     line1 = []
#     line2 = []
#     for i in range(5):
#         line1.append(me[i][i])
#         line2.append(me[0+i][4-i])
#     for l in range(5):
#         if cnt == 3:
#             break
#         if me[l] == O:
#             cnt += 1
#     for m in range(5):
#         col = []
#         for n in range(5):
#             col.append(me[n][m])
#         if cnt == 3:
#             break
#         if  col == O:
#             cnt += 1
#     if line1 == O:
#         if cnt == 3:
#             break
#         cnt += 1
#     if line2 == O:
#         if cnt == 3:
#             break
#         cnt += 1
#     if cnt != 3:
#         cnt = 0
#     k += 1
# print(result)

        
me = [list(map(int, input().split())) for n in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]
lst = []
for i in range(5):
    for j in range(5):
        lst.append(bingo[i][j])
cnt = 0
result = 10
k = 0
check = 0
while k != 10:
    for i in range(5):
        for j in range(5):
            if me[i][j] == lst[k]:
                me[i][j] = 0
                k += 1
                check = 1
                break
        if check == 1:
            check = 0
            break
while cnt != 3:
    for i in range(5):
        for j in range(5):
            if me[i][j] == lst[k]:
                me[i][j] = 0
                result += 1
                check = 1
                break
        if check == 1:
            check = 0
            break
    line1 = []
    line2 = []
    for i in range(5):
        line1.append(me[i][i])
        line2.append(me[0+i][4-i])
    for l in range(5):
        if me[l] == [0, 0, 0, 0, 0]:
            if cnt < 3:
                cnt += 1
    for m in range(5):
        col = []
        for n in range(5):
            col.append(me[n][m])
        if  col == [0, 0, 0, 0, 0]:
            if cnt < 3:
                cnt += 1
    if line1 == [0, 0, 0, 0, 0]:
        if cnt < 3:
            cnt += 1
    if line2 == [0, 0, 0, 0, 0]:
        if cnt < 3:
            cnt += 1
    if cnt != 3:
        cnt = 0
    k += 1
print(result)