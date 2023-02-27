# SW Expert Academy 0210_문제풀이2 - 1974    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1
    for i in range(9):
        num1 = 0
        num2 = 0
        for j in range(9):
            num1 += sudoku[i][j]
            num2 += sudoku[j][i]
        if num1 != 45 or num2 != 45:
            result = 0
            break
    for i in range(0, 7, 3):
        for l in range(0, 7, 3):
            num3 = 0
            for j in range(i, i+3):
                for k in range(l, l+3):
                    num3 += sudoku[j][k]
            if num3 != 45:
                result = 0
                break
    print(f'#{t}', result)
        
    