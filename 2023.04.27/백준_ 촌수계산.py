# 백준 2644 촌수계산

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
G = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
visited = [0]*(n+1)
Q = [p1]
check = 0
while Q:
    s = Q.pop(0)
    if s == p2:
        check = 1
        break
    for w in G[s]:
        if visited[w] == 0:
            Q.append(w)
            visited[w] = visited[s] + 1
if check == 0:
    print(-1)
else:
    print(visited[p2])
                