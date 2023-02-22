# SW Expert Academy 0207_List02 - 10760

import sys
sys.stdin = open('input.txt', 'r')

lst = ['(', ')', '{', '}']
T = int(input())
for t in range(1, T + 1):
    words = input()
    S = []
    top = -1
    result = 1
    for i in words:
        if i in lst:
            if top == -1:
                if i == ')' or i == '}':
                    result = 0
                    break
            if i == '(' or i == '{':
                S.append(i)
                top += 1
            elif i == ')':
                if S[top] == '(':
                    S.pop()
                    top -= 1
                else:
                    result = 0
                    break
            elif i == '}':
                if S[top] == '{':
                    S.pop()
                    top -= 1
                else:
                    result = 0
                    break
    if top != -1:
        result = 0
    print(f'#{t}', result)
                        
