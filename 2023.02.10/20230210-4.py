# SW Expert Academy 0210_문제풀이2 - 4751

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    char = input()
    arr = [[0]*((5*len(char))-len(char)+1) for _ in range(5)]
    i = 0
    m = 4
    k = 4
    l = 2
    while i < 2:
        for j in range(l, len(arr[0]), k):
            arr[i][j] = '#'
            arr[m][j] = '#'
        i += 1
        l -= 1
        k -= 2
        m -= 1
    for n in range(0, len(arr[2]), 4):
        arr[2][n] = '#'
    a = 0
    for i in range(2, len(arr[2]), 4):
        arr[2][i] = char[a]
        a += 1
    for i in range(len(arr)):
        for j in range((5*len(char))-len(char)+1):
            if arr[i][j] == 0:
                arr[i][j] = '.'

    for i in range(len(arr)):
        print(''.join(arr[i]))
