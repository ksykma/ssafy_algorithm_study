# SW Expert Academy 0206_List02 - 12390

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
A = [i for i in range(1, 13)]
for t in range(1, T+1):
    N, K = list(map(int, input().split()))
    subsets = [[]]
    for a in A:
        L = len(subsets)
        for l in range(L):
            result = subsets[l] + [a]
            subsets.append(result)

    count = 0
    for subset in subsets:
        if len(subset) == N and sum(subset) == K:
            count += 1
    print(f'#{t} {count}')



