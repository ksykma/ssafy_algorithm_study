# SW Expert Academy 0207_List02 - 12391

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    P, Pa, Pb = list(map(int, input().split()))
    def search(goal):
        l = 1
        r = P
        cnt = 0
        while l <= r:
            c = int((l+r)/2)
            if c == goal:
                return cnt
            elif c > goal:
                r = c
            else:
                l = c
            cnt += 1
    A = search(Pa)
    B = search(Pb)
    if A > B:
        print(f'#{t} B')
    elif A < B:
        print(f'#{t} A')
    else:
        print(f'#{t} 0')