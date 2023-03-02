# 백준 2578 빙고

import sys
sys.stdin = open('input.txt', 'r')

me = [list(map(int, input().split())) for n in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]
lst = []
for i in range(5):
    for j in range(5):
        lst.append(bingo[i][j])
cnt = 0
a = [n[2] for n in me]   # 특정 열 추출
result = 0
k = 0
check = 0
# for i in range(5):
#     a = [n[i] for n in me]
#     print(a)
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
            cnt += 1
    for m in range(5):
        if  a == [0, 0, 0, 0, 0]:
            cnt += 1
    if line1 == [0, 0, 0, 0, 0]:
        cnt += 1
    if line2 == [0, 0, 0, 0, 0]:
        cnt += 1
    if cnt != 3:
        cnt = 0
    k += 1
print(result)



# while cnt != 3:
#     for k in range(0, 25, 5):
#         lst_sum = sum(lst[k:k+5])
        
