# SW Expert Academy 0202_List01 - 12386

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    num = int(input())
    lst = input()
    cnt = [0] * 10
    for n in lst:
        cnt[int(n)] += 1
    max_val = 0
    max_c = 0
    for c in range(len(cnt)):
        if max_c <= cnt[c]:
            max_c = cnt[c]
            max_val = c
    print(f"#{t} {max_val} {max_c}")