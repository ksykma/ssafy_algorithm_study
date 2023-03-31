# SW Expert Academy 0330_분할_백트래킹 - 11896 백트래킹_전기버스2

import sys
sys.stdin = open('input.txt', 'r')

def bus(n, b, cnt):
    global ans
    if ans <= cnt:
        return
    if n == N:
        ans = min(ans, cnt)
    else:
        bus(n+1, lst[n]-1, cnt+1)
        
        if b > 0:
            bus(n+1, b-1, cnt)
            

T = int(input())
for t in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N
    bus(2, lst[1]-1, 0)
    print(f'#{t}', ans)