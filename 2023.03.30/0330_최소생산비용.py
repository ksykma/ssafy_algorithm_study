# SW Expert Academy 0330_분할_백트래킹 - 11897 최소 생산 비용

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    