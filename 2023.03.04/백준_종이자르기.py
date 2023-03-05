# 백준 2628 종이자르기

import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
w_cut = [0, w]
h_cut = [0, h]

for i in lst:
    if i[0] == 1:
        w_cut.append(i[1])
    else:
        h_cut.append(i[1])
w_cut.sort()
h_cut.sort()
ww = []
hh = []
for i in range(len(w_cut)-1):
    ww.append(w_cut[i+1]-w_cut[i])
for i in range(len(h_cut)-1):
    hh.append(h_cut[i+1]-h_cut[i])
max_val = 0
for i in range(len(ww)):
    for j in range(len(hh)):
        result = ww[i]*hh[j]
        if max_val < result:
            max_val = result
print(max_val)