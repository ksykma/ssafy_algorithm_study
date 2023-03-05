# 백준 10431 줄 세우기

import sys
sys.stdin = open('input.txt', 'r')

P = int(input())
for T in range(1, P+1):
    lst = list(map(int, input().split()))
    child = lst[1:]
    result = [child[0]]
    cnt = 0
    for i in range(1, 20):
        for j in range(len(result)):
            if result[j] > child[i]:
                cnt += len(result)-j
                result.insert(j, child[i])
                break
        else:
            result.append(child[i])
    print(T, cnt)