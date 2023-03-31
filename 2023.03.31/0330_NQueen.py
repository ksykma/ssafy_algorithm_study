# SW Expert Academy 0330_분할_백트래킹 - 2806 N-Queen

import sys
sys.stdin = open('input.txt', 'r')

def daegak(r, c):
    for i in range(r):
        if abs(i-r) == abs(cols[i] - c):
            return False
    return True

def Queen(k):
    global cnt
    if k == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if used[i] == 1:
                continue
            # k가 행 i 가 열
            if not daegak(k, i):
                continue
            used[i] = 1
            cols[k] = i
            Queen(k+1)
            used[i] = 0
            

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cols = [0] * N
    used = [0] * N
    cnt = 0
    Queen(0)
    print(f'#{t}', cnt)