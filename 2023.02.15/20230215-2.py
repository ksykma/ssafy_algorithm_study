# SW Expert Academy 0214_Stack1 - 1219  

import sys
sys.stdin = open('input.txt', 'r')
for t in range(10):
    T, E = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[] for _ in range(100)]   # 정점 번호 0 ~ 99
    # 간선 정보 읽기
    for i in range(0, E*2, 2):
        u, v = arr[i], arr[i+1]   # 유향 그래프이기 때문에 u->v만
        G[u].append(v)
    print(G)
    visited = [0] * 100
    S = [0]   # 출발점 추가
    visited[0] = 1
    v = 0
    while S:   # 빈 스택이 아닐동안
        # v의 방문하지 않은 인접정점 w를 하나 선택
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                S.append(v)
                v = w
                break
        else:
            v = S.pop()
    print(f'#{T}', visited[99])


# 재귀로 푸는법
# for t in range(10):
#     T, E = map(int, input().split())
#     arr = list(map(int, input().split()))

#     G = [[] for _ in range(100)]   # 정점 번호 0 ~ 99
#     # 간선 정보 읽기
#     for i in range(0, E*2, 2):
#         u, v = arr[i], arr[i+1]   # 유향 그래프이기 때문에 u->v만
#         G[u].append(v)

#     visited = [0] * 100
    
#     # 일단 이거라도 잘 이해하자고
#     def DFS(v):   # v: 현재 방문할 정점
#         visited[v] = 1
#         for w in G[v]:
#             if not visited[w]:
#                 DFS(w)

#     # 얘는 return으로 재귀함수 컨트롤 하는 법
#     # def DFS(v):   # v: 현재 방문할 정점
#     #     visited[v] = 1
#     #     if v == 99:
#     #         return 1
#     #     for w in G[v]:
#     #         if not visited[w]:
#     #             if DFS(w):   # 1이 반환되면 종료
#     #                 return 1
#     #     return 0

#     DFS(0)
#     print(visited[99])