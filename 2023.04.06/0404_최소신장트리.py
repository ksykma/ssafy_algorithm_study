# SW Expert Academy 0404_그래프 - 11900 그래프_최소 신장 트리

import sys
sys.stdin = open('input.txt', 'r')

def fine_set(x):
    while x != P[x]:
        x = P[x]
    return x
 
# 0번 ~ V번까지 노드.
T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    G = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        G.append((u, v, w))
    G.sort(key=lambda x:x[2])
    P = [i for i in range(V+1)]
    idx = 0
    cnt = 0
    for u, v, w in G:
        if fine_set(u) != fine_set(v):
            idx += 1
            P[fine_set(u)] = fine_set(v)
            cnt += w
            if idx == V: break
    print(f'#{t} {cnt}')