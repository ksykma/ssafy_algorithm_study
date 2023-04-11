# 백준 5597 과제 안 내신 분..?

import sys
sys.stdin = open('input.txt', 'r')

lst = [int(input()) for _ in range(28)]
total = [i for i in range(1, 31)]
for i in lst:
    total.remove(i)
print(min(total))
print(max(total))