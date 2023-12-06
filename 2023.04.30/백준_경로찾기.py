# 백준 2479 경로 찾기

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs():
    visited[A] = 1
    Q = deque()
    Q.append((A, str(A)))
    while Q:
        n, ans = Q.popleft()
        if n == B:
            return ans
        for i in range(1, N+1):
            cnt = 0
            if visited[i]:
                continue
            for j in range(K):
                if lst[n][j] != lst[i][j]:
                    cnt += 1
            if cnt == 1:
                visited[i] = 1
                Q.append((i, ans + ' ' + str(i)))

    return -1



N, K = map(int, input().split())
lst = ['0']+[input() for _ in range(N)]
A, B = map(int, input().split())
visited = [0] * (N+1)
print(bfs())