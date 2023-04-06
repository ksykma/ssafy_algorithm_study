# SW Expert Academy 0404_그래프 - 11902 그래프_최소 이동 거리

import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappop, heappush

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for i in range(E):
        s, e, weight = map(int, input().split())
        G[s].append((e, weight))
    print(G)
        
    Q = [(0, 0)]
    D = [0xfffff] * (N+1)
    D[0] = 0
    
    while Q:
        d, s = heappop(Q)
        if D[s] < d:
            continue
        for e, weight in G[s]:
            if D[e] > D[s] + weight:
                D[e] = D[s] + weight
                heappush(Q, (D[e], e))
    print(f'#{t}', D[N])
    