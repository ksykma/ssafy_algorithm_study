# 백준 14696 딱지놀이

import sys
sys.stdin = open('input.txt', 'r')

# 별 : 4 동: 3 네:2 세:1

N = int(input())

for n in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = A.pop(0)
    b = B.pop(0)
    A.sort(reverse=True)
    B.sort(reverse=True)
    check = 0
    for i in range(min(a, b)):
        if A[i] == B[i]:
            pass
        elif A[i] > B[i]:
            check = 1
            print('A')
            break
        elif A[i] < B[i]:
            check = 1
            print('B')
            break
    if check == 0:
        if a > b:
            print('A')
        elif a < b:
            print('B')
        else:
            print('D')