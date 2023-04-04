# SW Expert Academy 0330_분할_백트래킹 - 11896 백트래킹_전기버스2

import sys
sys.stdin = open('input.txt', 'r')

def money(n, result):
    global ans
    if n == C:
        ans = max(ans, result)
    else:
        money(n+1, result)

T = int(input())
for t in range(1, T + 1):
    num, C = map(int, input().split())
    ans = 0
    money(0, num)
