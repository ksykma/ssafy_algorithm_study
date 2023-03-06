# SW Expert Academy - 16811 당근 포장하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    minV = 1000
    for i in range(N-2): # 소박스
        for j in range(i+1, N-1): # 중박스
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]: # 같은 크기가 다른 박스에 들어가면 안돼
                A = i + 1
                B = j - i
                C = N - 1 - j
                if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2: # 빈박스 없고 절반 초과하는 박스가 없어야 돼
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)
    
    if minV == 1000:
        minV = -1
    print(f'#{t}', minV)