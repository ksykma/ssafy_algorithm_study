# 백준 2231 분해합

import sys
sys.stdin = open('input.txt', 'r')

while True:
    result = 'yes'
    num = input()
    if num == '0' :
        break
    for i in range(len(num) // 2):
        if num[i] != num[-i-1]:
            result = 'no'
    print(result)