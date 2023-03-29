# 백준 2804 크로스워드 만들기

import sys
sys.stdin = open('input.txt', 'r')

A, B = input().split()
arr = [['.']*len(A) for _ in range(len(B))]

lst = []
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            if A[i] not in lst:
                lst.append(A[i])
row = B.index(lst[0])
col = A.index(lst[0])
for i in range(len(A)):
    arr[row][i] = A[i]
for i in range(len(B)):
    arr[i][col] = B[i]

for i in range(len(B)):
    for j in range(len(A)):
        print(arr[i][j], end='')
    print()
