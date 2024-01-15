# 백준 13549 숨바꼭질3

from collections import deque
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [0] * 100001

#BFS 탐색
Q = deque()
Q.append(N) #시작 위치 추가

while Q:
    s = Q.popleft()
    if s == K:
        print(lst[s])
        break

    for i in (s*2, s-1, s+1):
        # 0~100000 사이에 존재하고 방문하지 않았으면
        if 0 <= i <= 100000 and not lst[i]:
            if i == s*2:
                lst[i] = lst[s]
            else:
                lst[i] = lst[s] + 1
            Q.append(i)
            