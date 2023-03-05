# 백준 2309 일곱 난쟁이

import sys
sys.stdin = open('input.txt', 'r')

lst = []
for i in range(9):
    lst.append(int(input()))
all = sum(lst)
minus = []
check = 0
for i in range(9):
    for j in range(i+1, 9):
        all -= lst[i]
        all -= lst[j]
        if all == 100:
            minus.append(lst[i])
            minus.append(lst[j])
            check = 1
            break
        else:
            all = sum(lst)
    if check == 1:
        break
for i in minus:
    lst.remove(i)
for i in sorted(lst):
    print(i)
