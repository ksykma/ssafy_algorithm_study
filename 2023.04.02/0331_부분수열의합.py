# SW Expert Academy 230331: 문제풀이_6 - 16898 부분 수열의 합 

import sys
sys.stdin = open('input.txt', 'r')

def buboon(n, result):
    global cnt
    if result > K:
        return
    if n == N:
        if result == K:
            cnt += 1
        return
    else:
        buboon(n+1, result+lst[n])
        buboon(n+1, result)
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    buboon(0, 0)
    print(f'#{t}', cnt)