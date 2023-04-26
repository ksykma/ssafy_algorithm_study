# 백준 2660 회장뽑기

import sys
sys.stdin = open('input.txt', 'r')

people = int(input())
G = [[] for _ in range(people+1)]
while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    G[u].append(v)
    G[v].append(u)
king = [0] * (people+1)
king[0] = 0xffffff
Q = []
for i in range(1, people+1):
    visited = [0] * (people+1)
    check = [0] * (people+1)
    Q.append(i)
    while Q:
        s = Q.pop(0)
        visited[s] = 1
        for w in G[s]:
            if visited[w] == 0:
                if check[w] == 0:
                    Q.append(w)
                    check[w] = check[s] + 1
    king[i] = max(check)
result = min(king)
print(result, king.count(result))
for i in range(1, people+1):
    if king[i] == result:
        print(i, end=' ')