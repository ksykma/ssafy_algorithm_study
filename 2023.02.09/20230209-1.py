# SW Expert Academy 0208_String - 12395

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    A, B = list(input().split())
    cnt = 0
    i = 0
    while i <= len(A)-len(B):
        for j in range(len(B)):
            if B[j] != A[i+j]:
                break
        else:
            cnt += 1
            i += len(B) - 1
        i += 1
    print(f'#{t} {len(A)-(len(B)*cnt)+cnt}')