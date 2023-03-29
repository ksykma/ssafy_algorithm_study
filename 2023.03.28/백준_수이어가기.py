# 백준 2635 수 이어가기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # 1 100
n = N // 2 # 2 62

max_val = 0
max_num = 0
result = []
for i in range(n, N+1):
    cnt = 1
    lst = [N]
    k = i # 62
    l = N # 100
    lst.append(k)
    while True:
        if cnt % 2 == 1:
            l -= k  # 38
            lst.append(l)
            if l < 0:
                if max_val < cnt:
                    max_val = cnt
                    max_num = i
                    result = lst
                break
            cnt += 1
        else:
            k -= l # 24
            lst.append(k)
            if k < 0:
                if max_val < cnt:
                    max_val = cnt
                    max_num = i
                    result = lst
                break
            cnt += 1
result.pop()
print(max_val+1)
print(*result)