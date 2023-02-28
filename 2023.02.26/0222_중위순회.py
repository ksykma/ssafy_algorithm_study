# SW Expert Academy 0222_Tree - 1231    

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    alpha = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)
    for i in range(N):
        lst = input().split()
        p = int(lst[0])
        if len(lst) == 3:
            L[p] = int(lst[2])
        elif len(lst) == 4:
            L[p] = int(lst[2])
            R[p] = int(lst[3])
        alpha[p] = lst[1]
        
    def inorder(i):
        if i:
            inorder(L[i])
            print(alpha[i], end = '')
            inorder(R[i])
        return
    print(f'#{t} ', end='')
    inorder(1)
    print()
    