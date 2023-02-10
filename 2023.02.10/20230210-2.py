# SW Expert Academy 0210_문제풀이2 - 1211

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    n = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    cnt_lst = []
    for i in range(102):
        if arr[0][i] == 1:
            cnt_lst.append(i)
    result = 0
    min_val = 100000
    for g in cnt_lst:
        h = 0
        cnt = 0
        idx = g
        while h < 99:
            h += 1
            cnt += 1
            if g == 1:
                if arr[h][g+1] == 1:
                    while arr[h][g] >= 1:
                        cnt += 1
                        g += 1
                    g -= 1
                    cnt -= 1
            elif g == 100:
                if arr[h][g-1] == 1:
                    while arr[h][g] >= 1:
                        cnt += 1
                        g -= 1
                    g += 1
                    cnt -= 1
            else:
                if arr[h][g-1] == 1:
                    while arr[h][g] >= 1:
                        cnt += 1
                        g -= 1
                    g += 1
                    cnt -= 1
                elif arr[h][g+1] == 1:
                    while arr[h][g] >= 1:
                        cnt += 1
                        g += 1
                    g -= 1
                    cnt -= 1

        if cnt < min_val:
            min_val = cnt
            result = idx

    print(f'#{t} {result-1}')