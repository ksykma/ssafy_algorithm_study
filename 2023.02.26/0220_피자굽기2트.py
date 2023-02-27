# SW Expert Academy 0220_Queue - 11650    

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    pizza = []
    Q = []
    for i in range(M):
        pizza.append([C[i], i+1])
    for i in range(N):
        Q.append(pizza[i])
    num = N
    while Q:
        [p, c] = Q.pop(0)
        p = p // 2
        result = c
        if p:
            Q.append([p, c])
        else:
            if num == M:
                pass
            else:
                Q.append(pizza[num])
                num += 1
    print(f'#{t}', result)