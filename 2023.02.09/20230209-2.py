# SW Expert Academy 0208_String - 12394

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    words = [list(input()) for _ in range(N)]
    lst = []
    for i in range(N):
        for j in range(N-M+1):
            r = 0
            for m in range(M//2):
                if words[i][j+m] == words[i][j+M-1-m]:
                    r += 1
                else:
                    r = 0
                    break
            if r == M // 2:
                for k in range(j, M + j):
                    lst.append(words[i][k])
                # print(('').join(words[i][j:]))

    for i in range(N):
        for j in range(N-M+1):
            r = 0
            for m in range(M//2):
                if words[j+m][i] == words[j+M-1-m][i]:
                    r += 1
                else:
                    r = 0
                    break
            if r == M // 2:
                for k in range(j, M + j):
                    lst.append(words[k][i])
    print(f'#{t}', end=' ')
    print(('').join(lst))
