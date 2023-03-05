# 백준 2477 참외밭

import sys
sys.stdin = open('input.txt', 'r')
cham = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
# 1 : 동 2 : 서 3 : 남 4 : 북
w = []
h = []
for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2:
        w.append(lst[i][1])
    else:
        h.append(lst[i][1])
w_max = max(w)
w_idx = 0
h_max = max(h)
h_idx = 0
for i in range(6):
    if lst[i][1] == w_max:
        w_idx = i
    if lst[i][1] == h_max:
        h_idx = i
w_minus = lst[(h_idx+3)%6][1]
h_minus = lst[(w_idx+3)%6][1]
total = w_max * h_max
minus = w_minus * h_minus
print((total-minus)*cham)