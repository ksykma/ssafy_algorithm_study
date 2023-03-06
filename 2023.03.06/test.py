# SW Expert Academy - 16811 당근 포장하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 당근개수
    arr = list(map(int, input().split()))
    arr.sort()
    minV = 1000
    for i in range(N-2):            # 소 박스
        for j in range(i+1, N-1):   # 중 박스
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                # 같은 크기가 다른 박스에 들어가는 경우 제외
                A = i+1
                B = j-1
                C = N-1-j
                if A*B*C != 0 and A<=N//2 and B<=N//2 and C<=N//2:
                # 빈 박스가 없고 절반 초과하는 박스도 없으면
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)

    if minV == 1000:
        minV = -1      # 포장할 수 없는 경우
    print(f'#{tc} {minV}')