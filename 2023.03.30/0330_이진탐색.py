# SW Expert Academy 0329_분할_백트래킹 - 11893 분할정복_이진탐색

import sys
sys.stdin = open('input.txt', 'r')

def binary_search(n, lst, key):
    global cnt, lst3
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == key:
            if len(lst3) == 0:
                cnt += 1
            return
        if lst[mid] > key:
            high = mid - 1
            lst3.append('l')

        elif lst[mid] < key:
            low = mid + 1
            lst3.append('r')

    return -1


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    a_lst = sorted(list(map(int, input().split())))
    b_lst = list(map(int, input().split()))
    cnt = 0
    for i in range(M):
        lst3 = []
        if b_lst[i] in a_lst:
            binary_search(N, a_lst, b_lst[i])
            if len(lst3) == 1:
                cnt += 1
            elif len(lst3) > 1:
                for j in range(len(lst3)-1):
                    if lst3[j] == lst3[j+1]:
                        break
                else:
                    cnt += 1

    print(f'#{t}', cnt)