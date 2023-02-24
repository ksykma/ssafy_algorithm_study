# SW Expert Academy 0224_문제풀이4 - 2117 홈 방범 서비스

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

k_lst = [((k*k)+(k-1)*(k-1)) for k in range(40)]
def solve_loop():
    result = 0
    for si in range(N):
        for sj in range(N):   # 가능한 모든 시작 위치
            for k in range(1, 2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    t = abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0 <= i < N and 0 <= j < N:
                            cnt += city[i][j]
                # 운영비용 보다 수익이 같거나 큰 경우 정답 갱신
                if k_lst[k] <= cnt * M:
                    result = max(result, cnt)
    return result

k_Lst = [k*k+(k-1)*(k-1) for k in range(26)]
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    city = [list(map(int, input().split())) for _ in range(N)]
    
    ans = solve_loop()
    print(ans)

    # def bfs(si, sj):
    #     q = []
    #     v = [[0]*N for _ in range(N)]

    #     q.append((si, sj))
    #     v[si][sj] = 1
    #     cnt = city[si][sj]   # 시작좌표가 집이면 1, 아니면 0

    #     while q:
    #         ci, cj = q.pop(0)
    #         for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    #             ni, nj = ci + di, cj + dj
    #             if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
    #                 q.append((ni, nj))
    #                 v[ni][nj] = v[ci][cj] + 1
    #                 cnt += city[ni][nj]
    # def solve_bfs():
    #     result = 0
    #     for si in range(N):
    #         for sj in range(N):
    #             result = max(result, bfs(si, sj))



    