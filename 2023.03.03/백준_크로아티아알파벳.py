# 백준 2941 크로아티아 알파벳

import sys
sys.stdin = open('input.txt', 'r')

lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
N = len(word)
for i in lst:
    if i in word:
        N = N-(len(i)-1)*word.count(i)
if 'dz=' and 'z=' in word:
    N += word.count('dz=')
print(N)