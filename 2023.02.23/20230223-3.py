# SW Expert Academy 0223_Tree - 12917   

import sys
sys.stdin = open('input.txt', 'r')
# T = int(input())
# for t in range(1, T + 1):
#     N, M, L = list(map(int, input().split()))
#     result = [0] * (N+1)
#     for i in range(M):
#         node, num = list(map(int, input().split()))
#         def inorder(v):
#             if v > N:
#                 return
#             inorder(v*2)
#             if v == node:
#                 result[node] = num
#             inorder(v*2+1)
#         inorder(1)
#     for i in range(N, 0, -1):
#         if result[i] == 0:
#             if i*2+1 > N:
#                 result[i] = result[i*2]
#             else:
#                 result[i] = result[i*2] + result[i*2+1]
#     print(f'#{t}', result[L])
    
    

T = int(input())

def inorder(v):
    if v > N : return 0
    l = inorder(2*v)
    r = inorder(2*v+1)
    if not node[v]:
        node[v] = l + r
    return node[v]

for tc in range(1, T+1):
    N, M, wants = map(int, input().split())
    # 1번은 루트 노드
    node = [0] * (N+1)
    for _ in range(M):
        lv, num = map(int, input().split())
        node[lv] = num
    inorder(1)

    print(f'#{tc}', node[wants])