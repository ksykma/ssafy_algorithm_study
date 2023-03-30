# SW Expert Academy 0327_완탐_탐욕 - 11891 병합정렬

import sys
sys.stdin = open('input.txt', 'r')
# 2 2 1 1 3
def func(s, e): # 2, 3
    if s == e:
        return
    
    mid = (s + e) // 2 # 1
    func(s, mid) # LEFT  10, 69
    func(mid+1, e) # RIGHT
    
    i, j, k = s, mid+1, s 
    # 
    
    # 비교해서 작은 값을 TMP에 넣어주기
    while i <= mid and j <= e:
        if lst[i] < lst[j]:  # LEFT가 더 작아
            tmp[k] = lst[i]
            i += 1
            k += 1
        else:  # RIGHT가 더 작아
            tmp[k] = lst[j]   
            j += 1
            k += 1
    
    # i, j, k = 1 2 2    
    while i <= mid:
        tmp[k] = lst[i] # [10, 69, ]
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
    lst = list(map(int, input().split()))  # 2 2 1 1 3
    tmp = [0] * N
    func(0, N-1)
