# SW Expert Academy 0215_Stack2 - 11620 

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    miro = [[1 for _ in range(N+2)]]
    for _ in range(N):
        miro.append([1]+list(map(int, input()))+[1])
    miro.append([1 for _ in range(N+2)])
    for i in range(N+2):
        for j in range(N+2):
            if miro[i][j] == 3:
                h = i
                w = j
            if miro[i][j] == 2:
                result1 = i
                result2 = j
                
    g1 = h
    g2 = w
    while g1 != result1 or g2 != result2:
        if miro[g1][g2+1] == 0 or miro[g1][g2+1] == 2:
            g2 += 1
            miro[g1][g2] = 1
        elif miro[g1][g2-1] == 0 or miro[g1][g2-1] == 2:
            g2 -= 1
            miro[g1][g2] = 1
        elif miro[g1+1][g2] == 0 or miro[g1+1][g2] == 2:
            g1 += 1
            miro[g1][g2] = 1
        elif miro[g1-1][g2] == 0 or miro[g1-1][g2] == 0:
            g1 -= 1
            miro[g1][g2] = 1
        else:
            print(f'#{t}', 0)
            break
    else:
        print(f'#{t}', 1)
