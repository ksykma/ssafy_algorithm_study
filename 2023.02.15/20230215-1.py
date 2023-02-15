# SW Expert Academy 0214_Stack1 - 12398  

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())   # V : 노드 수, E : 간선 수
    lst = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())   # S : 출발 노드, G : 도착 노드
    arr = [[] for _ in range(V+1)]
    for i in range(len(lst)):
        u, v = lst[i][0], lst[i][1]
        arr[u].append(v)
    visited = [0] * (V+1)
    stack = [1]
    visited[1] = 1
    while stack:
        for w in arr[S]:
            if not visited[w]:
                visited[w] = 1
                stack.append(S)
                S = w
                break
        else:
            S = stack.pop()
    print(f'#{t}', visited[G])