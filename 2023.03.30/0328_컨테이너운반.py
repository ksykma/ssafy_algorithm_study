# SW Expert Academy 0328_완탐_탐욕 - 11804 탐욕_컨테이너 운반

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    cnt = 0
    for i in range(M):
        for j in range(len(w)):
            if t[i] >= w[j]:
                a = w.pop(j)
                cnt += a
                break
    print(f'#{tc}', cnt)