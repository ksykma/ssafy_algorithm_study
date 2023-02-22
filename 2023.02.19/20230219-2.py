# SW Expert Academy 0207_List02 - 10760

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    words = input()
    S = []
    top = -1
    cal = ''
    for i in words:
        if i == '+':
            if top == -1:
                S.append(i)
                top += 1
            else:
                plus = S.pop()
                cal += plus
                S.append(i)
        else:
            cal += i
    if top != -1:
        for i in S:
            cal += i
            S.pop()
    for i in cal:
        if i == '+':
            b = S.pop()
            a = S.pop()
            S.append(a + b)
        else:
            S.append(int(i))
    print(f'#{t}', S[0])
    