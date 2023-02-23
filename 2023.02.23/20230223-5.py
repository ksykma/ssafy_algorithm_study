# SW Expert Academy 0223_Tree - 1232    

import sys
sys.stdin = open('input.txt', 'r')


for t in range(1, 11):
    N = int(input())
    lst = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)
    for i in range(N):
        nodes = input().split()
        if len(nodes) == 4:
            p = int(nodes[0])
            y = nodes[1]
            l = int(nodes[2])
            r = int(nodes[3])
            lst[p] = y
            L[p] = l
            R[p] = r
        if len(nodes) == 2:
            n = int(nodes[0])
            lst[n] = int(nodes[1])
    def inorder(v):
        if v == 0:
            return 0
        left = inorder(L[v])
        right = inorder(R[v])
        if lst[v] == '-':
            return left - right
        elif lst[v] == '+':
            return left + right
        elif lst[v] == '*':
            return left * right
        elif lst[v] == '/':
            return left / right
        else:
            return lst[v]
    print(f'#{t}', int(inorder(1)))
    
    