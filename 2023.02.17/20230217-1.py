# SW Expert Academy 0215_Stack2 - 12390

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    arr_set = [[]]
    lst = []
    for i in A:
        len_set = len(arr_set)
        for j in range(len_set):
            arr_set.append(arr_set[j]+[i])
    for i in arr_set:
        if len(i) == N and sum(i) == K:
            lst.append(i)
    if len(lst) > 0:
        print(f'#{t}', len(lst))
    else:
        print(f'#{t}', 0)


