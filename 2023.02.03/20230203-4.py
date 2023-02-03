# SW Expert Academy 0202_List01 - 9367

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    result = 0
    max_val = 0
    for c in range(N-1):
        if C[c + 1] > C[c]:
            result += 1
        else:
            result = 0
        if result > max_val:
            max_val = result
    max_val += 1
    print(f"#{t} {max_val}")
