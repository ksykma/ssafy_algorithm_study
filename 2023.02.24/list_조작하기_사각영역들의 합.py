# SW Expert Academy List(Array)_조작하기 - 11012    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(M):
        lst = list(map(int, input().split()))
        h = lst[0]+lst[2]
        w = lst[1]+lst[2]
        if h > N:
            h = N
        if w > N:
            w = N
        for j in range(lst[0], h):
            for k in range(lst[1], w):
                if arr2[j][k] == 0:
                    cnt += arr[j][k]
                    arr2[j][k] += 1

    print(f'#{t}', cnt)
