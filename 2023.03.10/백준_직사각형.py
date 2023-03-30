# 백준 2527 직사각형

import sys
sys.stdin = open('input.txt', 'r')

for t in range(4):
    ax, ay, ap, aq, bx, by, bp, bq = list(map(int, input().split()))
    if ax > bp or ay > bq or ap < bx or aq < by:
        print('d')
    elif ax == bp or ap == bx:
        if ay != bq and aq != by:
            print('b')
        else:
            print('c')
    elif ay == bq or aq == by:
        if ap != bx and ax != bp:
            print('b')
        else:
            print('c')
    else:
        print('a')