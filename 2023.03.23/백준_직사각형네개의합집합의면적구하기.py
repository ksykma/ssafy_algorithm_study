# 백준 2669 직사각형 네개의 합집합의 면적 구하기

import sys
sys.stdin = open('input.txt', 'r')

arr = [[0]*101 for _ in range(101)]
for i in range(4):
    rec = list(map(int, input().split()))
    for j in range(rec[0], rec[2]):
        for k in range(rec[1], rec[3]):
            arr[j][k] = 1
result = 0
for i in range(101):
    result += arr[i].count(1)
print(result)