# SW Expert Academy 0303_문제풀이5 - 1860

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    max_val = 0
    for i in arr:
        if len(i) > max_val:
            max_val = len(i)
    for j in arr:
        if len(j) < max_val:
            while len(j) != max_val:
                j.append('')
    result = ''
    for j in range(max_val):
        for i in range(5):
            result += arr[i][j]
    print(f'#{t}', result)