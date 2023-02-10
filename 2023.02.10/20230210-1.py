# SW Expert Academy 0210_문제풀이2 - 1961

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    lst1 = []
    lst2 = []
    lst3 = []

    # 90도

    for i in range(N):
        num = ''
        for j in range(N-1, -1, -1):
            num += arr[j][i]
        lst1.append(num)
        num = ''

    # 180도
    for i in range(N-1, -1, -1):
        num = ''
        for j in range(N-1, -1, -1):
            num += arr[i][j]
        lst2.append(num)
        num = ''

    # 270도
    for i in range(N-1, -1, -1):
        num = ''
        for j in range(N):
            num += arr[j][i]
        lst3.append(num)
        num = ''
    print(f'#{t}')
    for l in range(N):
        print(lst1[l], lst2[l], lst3[l])
