# SW Expert Academy 0213_Stack1 - 1217 

import sys
sys.stdin = open('input.txt', 'r')
def function(A, B):
    if B == 0:
        return 1
    B -= 1
    return A * function(A, B)

for t in range(1, 11):
    T = int(input())
    A, B = list(map(int, input().split()))
    print(f'#{T}', function(A, B))

