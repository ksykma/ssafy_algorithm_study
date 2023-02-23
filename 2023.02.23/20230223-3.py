# SW Expert Academy 0223_Tree - 12917   

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    # left = [0] * (N+1)
    # right = [0] * (N+1)
    # P = [0] * (N+1)
    result = [0] * (N+1)
    for i in range(M):
        node, num = list(map(int, input().split()))
    #     for j in range(N+1):
    #         if j == node:
    #             if left[node] == 0:
    #                 left[node] = num
    #             elif right[node] == 0:
    #                 right[node] = num
    #             P[j] = j
    # print(left, right)
        def inorder(v):
            if v > N:
                return
            inorder(v*2)
            if v == node:
                result[v] = num
            inorder(v*2+1)
        inorder(1)
    print(result)