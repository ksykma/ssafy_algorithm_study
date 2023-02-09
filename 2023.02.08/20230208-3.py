# SW Expert Academy 0208_String - 1221

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    num, length = list(input().split())
    words = list(input().split())
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_lst = []
    for i in number:
        cnt = 0
        for j in words:
            if i == j:
                cnt += 1
        cnt_lst.append(cnt)
    print(num)
    for k in range(len(number)):
        print((number[k] + ' ') * cnt_lst[k])
    
