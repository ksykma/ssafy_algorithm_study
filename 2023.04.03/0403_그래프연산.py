# SW Expert Academy 0403_그래프 - 11898 그래프_연산

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def cal(N):
    while Q:
        s = Q.popleft()
        for i in (1, -1, 2, -10):
            if i == 2:
                p = s*i
            else:
                p = s+i
            if 0 < p <= 1000000 and visited[p] == 0:
                Q.append(p)
                visited[p] = visited[s] + 1
            if p == M:
                return s

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Q = deque()
    Q.append(N)
    visited = [0]*1000001
    visited[N] = 1
    print(f'#{t}', visited[cal(N)])
    

