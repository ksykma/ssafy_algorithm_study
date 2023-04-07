# SW Expert Academy 0404_그래프 - 11900 그래프_최소 신장 트리

import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappop, heappush

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
    Q = [(0, 0)]
    D = [0xfffff] * (V+1)
    D[0] = 0
    # visit = [0]*(V+1)
    while Q:
        d, u = heappop(Q)
        # visit[s] = 1
        if D[u] < d:
            continue
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(Q, (D[v], v))
    print(f'#{t}', D[V])
            