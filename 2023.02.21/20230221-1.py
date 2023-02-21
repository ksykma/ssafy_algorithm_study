# SW Expert Academy 0221_Queue - 11651 

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# def enQueue(item):
#     global rear
#     rear = rear + 1
#     Q[rear] = item

# def deQueue():
#     global front
#     front = front + 1
#     return Q[front]

# T = int(input())
# for t in range(1, T + 1):
#     V, E = map(int, input().split())   # 노드, 간선 개수
#     nums = [list(map(int, input().split())) for _ in range(E)]   # 간선의 양쪽 노드
#     S, G = map(int, input().split())   # 출발, 도착 노드
#     front = -1
#     rear = -1
#     Q = [0] * (V + 1)   # 큐
#     D = [0] * (V + 1)   # 출발점에서 각 정점까지 최단거리
#     P = [0] * (V + 1)   # 최단경로트리
#     lst = [[] for _ in range(V + 1)]   # 인접리스트
#     for i in range(E):
#         u, v = nums[i][0], nums[i][1]
#         lst[u].append(v)
#         lst[v].append(u)
        
#     visited = [0] * (V + 1)
#     visited[S] = 1
#     enQueue(S)
#     while front != rear:
#         s = deQueue()
#         for w in lst[s]:
#             if not visited[w]:
#                 enQueue(w)
#                 visited[w] = 1
#                 D[w] = D[s] + 1
#                 P[w] = s
#     print(f'#{t}', D[G])

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())   # 노드, 간선 개수
    nums = [list(map(int, input().split())) for _ in range(E)]   # 간선의 양쪽 노드
    S, G = map(int, input().split())   # 출발, 도착 노드
    front = -1
    rear = -1
    lst = [[] for _ in range(V + 1)]
    Q = deque([])
    D = [0] * (V + 1)
    visited = [0] * (V + 1)
    visited[S] = 1
    Q.append(S)
    for i in range(E):
        u, v = nums[i][0], nums[i][1]
        lst[u].append(v)
        lst[v].append(u)
    while Q:
        s = Q.popleft()
        for w in lst[s]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1
                D[w] = D[s] + 1
    print(f'#{t}', D[G])