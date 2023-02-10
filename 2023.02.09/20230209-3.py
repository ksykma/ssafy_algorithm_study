# SW Expert Academy 0208_String - 1974

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    # 가로
    for i in range(9):
        sum_result = 0
        for j in range(9):
            sum_result += puzzle[i][j]
        if sum_result != 45:
            cnt += 1
            break

    if cnt > 0:
        print(f'#{t} 0')
        cnt = 0
        continue
    # 세로
    for i in range(9):
        sum_result = 0
        for j in range(9):
            sum_result += puzzle[j][i]
        if sum_result != 45:
            cnt += 1
            break

    if cnt > 0:
        print(f'#{t} 0')
        cnt = 0
        continue
    # 3 * 3
    for i in range(0, 9, 3):    
        sum_result = 0
        for j in range(i, i + 3):
            for k in range(i, i + 3):
                sum_result += puzzle[j][k]
        if sum_result != 45:
            cnt += 1
            break
    if cnt == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
        
            








    # 가로
    # for k in range(9):
    #     for i in range(8):
    #         min_val = i
    #         for j in range(i+1, 9):
    #             if puzzle[k][min_val] > puzzle[k][j]:
    #                 min_val = j
    #         puzzle[k][i], puzzle[k][min_val] = puzzle[k][min_val], puzzle[k][i]
    #     if puzzle[k] == lst:
    #         cnt += 1
    #     else:
    #         break
    #     # 세로
    # for k in range(9):
    #     for i in range(8):
    #         min_val = k
    #         for j in range(k+1, 9):
    #             if puzzle[i][min_val] > puzzle[i][j]:
    #                 min_val = j
    #         puzzle[i][k], puzzle[i][min_val] = puzzle[i][min_val], puzzle[i][k]
    #     if puzzle[i] == lst:
    #         cnt += 1
    #     else:
    #         break
        # 네모

    
