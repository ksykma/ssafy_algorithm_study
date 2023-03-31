# SW Expert Academy 0328_완탐_탐욕 - 1244 최대 상금

import sys
sys.stdin = open('input.txt', 'r')

d = [1, 10, 100, 1000, 10000, 100000]
T = int(input())
for t in range(1, T + 1):
    nums, c = map(int, input().split())
    visit = [set() for _ in range(c+1)]
    visit[0].add(nums)
    N = len(str(nums))
    for h in range(1, c + 1):
        for nums in visit[h - 1]:
            for i in range(N - 1):
                for j in range(i + 1, N):
                    a = (nums // d[i]) % 10
                    b = (nums // d[j]) % 10
                    val = nums - a * d[i] + a * d[j] - b * d[j] + b * d[i]
                    visit[h].add(val)

    print(max(visit[c]))