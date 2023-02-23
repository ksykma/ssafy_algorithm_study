# SW Expert Academy 0222_Tree - 1231  

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    alpha = [0] * (N + 1)
    for i in range(N):
        arr = input().split()
        p = int(arr[0])
        if len(arr) == 3:
            L[p] = int(arr[2])
        elif len(arr) == 4:
            L[p] = int(arr[2])
            R[p] = int(arr[3])
        alpha[p] = arr[1]

    def inorder(i):
        if i:
            inorder(L[i])
            print(alpha[i], end = '')
            inorder(R[i])
        return
    print(f'#{t} ', end='')
    inorder(1)
    print()
    