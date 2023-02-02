# SW Expert Academy 0201_List01 - 12383

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_val = 0
    for i in range(len(lst)):
        count = 0
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                count += 1
        if max_val < count:
            max_val = count
    print(f"#{t} {max_val}")
