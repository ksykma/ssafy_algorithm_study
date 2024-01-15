# 백준 11723 집합

import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())
S = set()
for i in range(N):
    given = list(input().split())
    if len(given) == 2:
        if given[0] == 'add':
            S.add(int(given[1]))
        elif given[0] == 'remove':
            if int(given[1]) in S:
                S.remove(int(given[1]))
        elif given[0] == 'check':
            if int(given[1]) in S:
                print(1)
            else:
                print(0)
        elif given[0] == 'toggle':
            if int(given[1]) in S:
                S.remove(int(given[1]))
            else:
                S.add(int(given[1]))
    else:
        if given[0] == 'all':
            S = set([i for i in range(1,21)])
        elif given[0] == 'empty':
            S = set()