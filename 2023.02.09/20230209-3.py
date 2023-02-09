# SW Expert Academy 0208_String - 1974

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    puzzle = [list(input().split()) for _ in range(9)]
    lst = [k for k in range(1, 10)]
    for i in range(9):
        cnt = 0
        for j in range(9):
            for k in lst:
                if puzzle[i][j] == k:
                    cnt += 1
                else:
                    pass
        
        if cnt == 9:
            pass
        else:
            break
    