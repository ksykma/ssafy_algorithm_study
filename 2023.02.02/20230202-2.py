# SW Expert Academy 0202_List01 - 1204

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    num = int(input())
    lst = list(map(int, input().split()))
    cnt = [0] * 101
    for i in range(len(lst)):
        cnt[lst[i]] += 1
    max_val = 0
    for k in range(len(cnt)-1):
        if cnt[max_val] <= cnt[k]:
            max_val = k
    print(f"#{t} {max_val}")


        