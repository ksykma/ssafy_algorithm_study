# SW Expert Academy 0222_Tree - 12914    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    E, N = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    P = [0] * (E+2)
    L = [0] * (E+2)
    R = [0] * (E+2)
    for i in range(0, E*2, 2):
        p, c = lst[i], lst[i+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p
    print(L)
    print(R)
    def subtree(v):
        if v == 0:
            return 0
        l = subtree(L[v])
        r = subtree(R[v])
        return l + r + 1
    print(f'#{t}', subtree(N))