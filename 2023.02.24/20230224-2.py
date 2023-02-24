# SW Expert Academy 0223_Tree - 12917   

import sys
sys.stdin = open('input.txt', 'r')
# 각 정류장에 몇개의 버스노선?
T = int(input())
for t in range(1, T + 1):
    N = int(input())   # 버스노선 개수
    # i번째 버스노선은 A이상 B이하의 모든 정류장을 다님
    bus = 5001 * [0]
    for i in range(N):   # i번째 버스 노선 A이상, B이하
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bus[j] += 1
    P = int(input())   # 버스정류장 개수
    result = []
    for i in range(P):
        c = int(input())
        result.append(bus[c])
    
    print(f'#{t}', *result)
