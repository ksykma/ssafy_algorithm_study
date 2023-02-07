# SW Expert Academy 2차배열순회 - 12392

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_val = 0
    min_val = 100
    result = []
    count = 0
    while count < 5:
        for i in lst:
            if i > max_val:
                max_val = i
            if i < min_val:
                min_val = i
        result.append(max_val)
        result.append(min_val)
        lst.remove(max_val)
        lst.remove(min_val)
        max_val = 0
        min_val = 100
        count += 1
    print(f'#{t}', *result)

