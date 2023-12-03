# 백준 1753 최단경로

import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappop, heappush

V, E = map(int, input().split())
K = int(input())
lst = [list(map(int, input().split())) for _ in range(E)]
G = [[] for _ in range(V+1)]
for e in range(E):
    u = lst[e][0]
    v = lst[e][1]
    w = lst[e][2]
    G[u].append([v, w])

for i in range(1, V+1):
    Q = [(0, 1)] # 시작점(d, 정점번호)
    D = [0xfffff] * (V+1)
    D[1] = 0
    visited = [0] * (V+1)

    while Q:
        d, s = heappop(Q)
        if visited[s]:
            continue
        visited[s] = 1
        for g in G[s]:
            v = g[0]
            w = g[1]
            if not visited[v] and D[v] > D[s] + w:
                D[v] = D[s] + w
                heappush(Q, (D[v], v))
    if D[i] == 0xfffff:
        D[i] = "INF"
    print(D[i])
