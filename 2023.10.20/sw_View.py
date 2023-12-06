# sw아카데미 View

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    view = 0
    for i in range(2, N-2):
        lst2 = [lst[i-2], lst[i-1], lst[i+1], lst[i+2]]
        cnt = 0
        for j in lst2:
            if lst[i] > j:
                cnt += 1
        if cnt == 4:
            view += lst[i] - max(lst2)
    print(f"#{t} {view}")