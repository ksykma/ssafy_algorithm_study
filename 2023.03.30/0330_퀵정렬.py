# SW Expert Academy 0329_분할_백트래킹 - 11892 분할정복_퀵정렬

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def quick_sort(l, r):
    if l >= r:
        return
    i, j = l, r
    p = lst[l]
    while i <= j:
        while i <= r and p >= lst[i]:
            i += 1
        while p < lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            
    lst[l], lst[j] = lst[j], lst[l]
    quick_sort(l, j - 1)
    quick_sort(j + 1, r)


for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(0, len(lst)-1)
    print(f'#{t}', lst[N//2])