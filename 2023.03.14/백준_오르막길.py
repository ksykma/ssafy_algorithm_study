# 백준 2846 오르막길

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))

orumakgil = []
max_val = 0
for i in range(N-1):
    if lst[i] < lst[i+1]:
        if lst[i] not in orumakgil:
            orumakgil.append(lst[i])
        if lst[i+1] not in orumakgil:
            orumakgil.append(lst[i+1])
    else:
        if len(orumakgil) != 0:
            result = max(orumakgil) - min(orumakgil)
            if max_val < result:
                max_val = result
            orumakgil = []
if len(orumakgil) != 0:
    result = max(orumakgil) - min(orumakgil)
    if max_val < result:
        max_val = result
        
print(max_val)
