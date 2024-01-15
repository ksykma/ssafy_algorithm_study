# 백준 22233 가희와 키워드
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
keyword = {sys.stdin.readline().rstrip() : 0 for _ in range(N)}
answer = N
for i in range(M):
    essay = list(sys.stdin.readline().rstrip().split(","))
    for j in essay:
        if j in keyword.keys():
            if keyword[j] == 0:
                answer -= 1
                keyword[j] = 1
    print(answer)