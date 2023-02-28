# SW Expert Academy 0221_Queue - 11651    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    V, E = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))
    visited = [0] * (V+1)
    load = [[] for _ in range(V+1)]
    Q = [S]
    D = [0] * (V+1)
    for i in range(E):
        u, v = lst[i][0], lst[i][1]
        load[u].append(v)
        load[v].append(u)
    while Q:
        s = Q.pop(0)
        for w in load[s]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[s] + 1

    print(f'#{t}', visited[G])
