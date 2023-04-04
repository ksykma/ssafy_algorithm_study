# SW Expert Academy 230331: 문제풀이_6 - 14119 수영장

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    swim = list(map(int, input().split()))
    ans = [0]*12
    for i in range(12):
        if i == 0:
            ans[i] = swim[i]*day
            ans[i] = min(ans[i], month)
        else:
            ans[i] = ans[i-1] + swim[i]*day
            ans[i] = min(ans[i], ans[i-1]+month)
        if i >= 2:
            ans[i] = min(ans[i], ans[i-3]+month3)
        if i >= 11:
            ans[i] = min(ans[i], year)
    print(f'#{t}', ans[11])
