# SW Expert Academy 0327_완탐_탐욕 - 11891 병합정렬

import sys
sys.stdin = open('input.txt', 'r')

def func(s, e):
    if s == e:
        return
    mid = (s + e) // 2
    func(s, mid)
    func(mid+1, e)
    i, j, k= s, mid+1, s
    while i <= mid and j <= e:
        if lst[i] < lst[j]:
            tmp[k] = lst[i]
            i += 1
        else:
            tmp[k] = lst[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = lst[i]
        k += 1
        i += 1
    while j <= e:
        tmp[k] = lst[j]
        j += 1
        k += 1
    for i in range(s, e+1):
        lst[i] = tmp[i]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    tmp = [0] * N
    func(0, N-1)
    print(lst)

