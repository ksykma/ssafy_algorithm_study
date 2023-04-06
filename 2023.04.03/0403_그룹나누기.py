# SW Expert Academy 0403_그래프 - 11899 그래프_그룹나누기

import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w)

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        u, v = nums[i], nums[i+1]
        G[u].append(v)
        G[v].append(u)
    
    visited = [0] * (N+1)
    ans = 0
    for i in range(1, N+1):
        if visited[i] == 1:
            continue
        ans += 1
        dfs(i)
    print(f'#{t}', ans)