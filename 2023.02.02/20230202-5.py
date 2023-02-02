# SW Expert Academy 0202_List01 - 1208

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    num = int(input())
    lst = list(map(int, input().split()))

    for n in range(num):
        max_val = 0
        max_idx = 0
        min_val = 100
        min_idx = 100
        for i in range(len(lst)):
            if max_val <= lst[i]:
                max_val = lst[i]
                max_idx = i
            if min_val >= lst[i]:
                min_val = lst[i]
                min_idx = i
        lst[max_idx] -= 1
        lst[min_idx] += 1
    print(lst)
    max_lst = 0
    min_lst = 100
    for j in lst:
        if max_lst <= j:
            max_lst = j
        if min_lst >= j:
            min_lst = j
    print(f"#{t} {max_lst - min_lst}")