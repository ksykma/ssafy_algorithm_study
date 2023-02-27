# SW Expert Academy List(Array)_조작하기 - 11013   

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    min_val = 10000
    for i in range(1, N-1):
        for j in range(i+1, N):
            result = [sum(lst[:i]), sum(lst[i:j]), sum(lst[j:])]
            ans = max(result) - min(result)
            if min_val > ans:
                min_val = ans
    print(f'#{t}', min_val)