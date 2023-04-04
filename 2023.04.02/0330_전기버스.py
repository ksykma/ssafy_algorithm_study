# SW Expert Academy 0330_분할_백트래킹 - 11896 백트래킹_전기버스2

import sys
sys.stdin = open('input.txt', 'r')

def bus(n, battery, cnt):
    global ans
    if ans <= cnt:
        return
    if n == N:
        ans = min(ans, cnt)
    else:
        bus(n+1, stop[n]-1, cnt+1)
        if battery > 0:
            bus(n+1, battery-1, cnt)

T = int(input())
for t in range(1, T + 1):
    stop = list(map(int, input().split()))
    N = stop[0]
    ans = 0xfffff
    bus(2, stop[1]-1, 0)
    print(f'#{t}', ans)