# 백준 10988 팰린드롬인지 확인하기

import sys
sys.stdin = open('input.txt', 'r')

word = input()
N = len(word)
ans = 1
for i in range(N//2):
    if word[i] != word[-i-1]:
        ans = 0
        break

print(ans)