# SW Expert Academy 0209_String - 1215 회문1

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0
    # 가로
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                a = arr[i][j+k]
                b = arr[i][j+N-1-k]
                if a != b:
                    break
            else:
                cnt += 1
    # 세로
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                a = arr[j+k][i]
                b = arr[j+N-1-k][i]
                if a != b:
                    break
            else:
                cnt += 1
    print(f'#{t}', cnt)