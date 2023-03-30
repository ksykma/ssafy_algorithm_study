# SW Expert Academy 0327_완탐_탐욕 - 11891 병합정렬

import sys
sys.stdin = open('input.txt', 'r')

def func(lst):
    global cnt
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = func(lst[:mid])
    right = func(lst[mid:])
    ret = []
    if left[-1] > right[-1]:
        cnt += 1
    l, r = len(left), len(right)
    idx_l, idx_r = 0, 0
    while idx_l < l and idx_r < r:
        if left[idx_l] < right[idx_r]:
            ret.append(left[idx_l])
            idx_l += 1
        else:
            ret.append(right[idx_r])
            idx_r += 1
    ret.extend(left[idx_l:])
    ret.extend(right[idx_r:])
    return ret
    

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    print(f'#{t}', func(lst)[N//2], cnt)
    


