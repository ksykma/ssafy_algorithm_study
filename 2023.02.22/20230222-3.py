 # SW Expert Academy 0221_Queue - 1238 

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

for t in range(1, 11):
    N, S = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(0, N, 2):
        a, b = lst[i], lst[i+1]
        G[a].append(b)
    Q = deque([])
    visited = [0] * 101
    Q.append(S)
    visited[S] = 1
    result = []
    while Q:
        s = Q.popleft()
        for w in G[s]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[s] + 1
    max_val = max(visited)
    for i in range(101):
        if visited[i] == max_val:
            result.append(i)
    print(f'#{t}', max(result))
