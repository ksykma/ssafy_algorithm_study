# SW Expert Academy 0327_완탐_탐욕 - 11803 완전검색_전기카트
import sys
sys.stdin = open('input.txt', 'r')

def golf(n, cnt):
    global ans
    if ans <= cnt:
        return
    if n == N:
        cnt += arr[check[N-1]][0]
        ans = min(ans, cnt)
    else:
        for i in range(1, N):
            if visit[i] == 1:
                continue
            visit[i] = 1
            check[n] = i
            golf(n+1, cnt+arr[check[n-1]][i])
            visit[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    check = [0] * N
    ans = 0xfffff
    golf(1, 0)
    print(f'#{t}', ans)
    