# 백준 2606 바이러스

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
band = int(input())
G = [[] for _ in range(N+1)]
for i in range(band):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
Q = [1]
visited = [0]*(N+1)
while Q:
    s = Q.pop(0)
    if visited[s] == 1:
        continue
    else:
        visited[s] = 1
        for i in range(len(G[s])):
            Q.append(G[s][i])
print(sum(visited)-1)