# SW Expert Academy 0201_List01 - 12387    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))   # 정수의 개수, 구간의 개수
    lst = list(map(int, input().split()))
    min_val = 10000 * N
    max_val = 0
    num = 0
    for i in range(N - M + 1):
        for j in range(M):
            num += lst[i+j]
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        num = 0
    print(f'#{t}', max_val - min_val)