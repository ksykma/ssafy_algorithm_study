# 백준 2810 컵홀더

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
sit = input()
cup = N+1
cnt = sit.count('LL')
cup -= cnt
if cup > N:
    print(N)
else:
    print(cup)