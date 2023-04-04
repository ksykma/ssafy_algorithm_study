# SW Expert Academy 0331_문제풀이6 - 5215 햄버거 다이어트

import sys
sys.stdin = open('input.txt', 'r')
 
def hamburger(n, score1, cal1):
    global ans
    if score1 <= ans:
        return
    if cal1 <= L:
        if score1 > ans:
            ans = score1
        return
    for i in range(n, -1, -1):
        if used[i] == 0:
            continue
        used[i] = 0
        hamburger(i - 1, score1 - score_lst[i], cal1 - cal_lst[i])
        used[i] = 1

T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    score_lst = []
    cal_lst = []
    for i in range(N):
        score, cal = map(int, input().split())
        score_lst.append(score)
        cal_lst.append(cal)
    ans = 0
    used = [1] * N
    hamburger(N-1, sum(score_lst), sum(cal_lst))
    print(f'#{t}', ans)