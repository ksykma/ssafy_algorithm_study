# SW Expert Academy 0217_문제풀이3 - 10760

import sys
sys.stdin = open('input.txt', 'r')
icp = {'+' : 1, '*' : 2, '(' : 3, ')' : 0}
isp = {'+' : 1, '*' : 2, '(' : 0, ')' : 0}
for t in range(1, 11):
    N = int(input())
    words = input()
    S = []
    char = ''
    for i in words:
        if i in icp:
            if i == ')':
                while S[-1] != '(':
                    char += S.pop()
                S.pop()
            else:
                while S and isp[S[-1]] >= icp[i]:
                    char += S.pop()
                S.append(i)
        else:
            char += i
    while S:
        char += S.pop()
    for i in char:
        if i == '+':
            b = S.pop()
            a = S.pop()
            S.append(a + b)
        elif i == '*':
            b = S.pop()
            a = S.pop()
            S.append(a * b)
        else:
            S.append(int(i))
    print(f'#{t}', S[0])