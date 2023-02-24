# SW Expert Academy 0223_Tree - 12917   

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    result = [0] * (N+1)
    for i in range(M):
        node, num = list(map(int, input().split()))
        result[node] = num
    for i in range(N, 0, -1):
        if result[i] == 0:
            if i*2+1 > N:   # i의 오른쪽 자식 값이 범위를 벗어나면
                result[i] = result[i*2]   
            else:
                result[i] = result[i*2] + result[i*2+1]
    print(f'#{t}', result[L])