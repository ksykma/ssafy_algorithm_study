# SW Expert Academy 0209_String - 1216 회문2

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    max_val = 0
    # 가로
    for i in range(100):
        for j in range(100):
            for k in range(100):
                for l in range(100):
                    a = arr[i][j+k]
                    b = arr[i][j+100-1-k-l]
                    if a != b:
                        break
            else:
                if max_val < 
    # 세로
    for i in range(100):
        for j in range(100-N+1):
            for k in range(N//2):
                a = arr[j+k][i]
                b = arr[j+N-1-k][i]
                if a != b:
                    break
            else:
                cnt += 1
    print(f'#{t}', cnt)