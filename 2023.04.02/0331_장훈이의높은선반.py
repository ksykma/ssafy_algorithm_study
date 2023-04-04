# SW Expert Academy 230331: 문제풀이_6 - 14034 장훈이의 높은 선반

import sys
sys.stdin = open('input.txt', 'r')

def top(n, cnt):
    global ans
    if cnt >= B:
        ans = min(ans, cnt)
        return
    if n == N:
        if cnt >= B:
            ans = min(ans, cnt)
            return
    else:
        top(n+1, cnt+lst[n])
        top(n+1, cnt)
        

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0xfffff
    top(0, 0)
    print(f'#{t}', ans - B)