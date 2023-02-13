# SW Expert Academy 0213_Stack1 - 12396

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
def push(item):
    global top
    top += 1
    S[top] = item
def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

for t in range(1, T + 1):
    lst = list(input())
    S = [0] * len(lst)
    top = -1
    result = 1
    for i in lst:
        if i != '{' and i != '}' and i != '(' and i != ')':
            continue
        if i == '{' or i == '(':
            push(i)
        else:
            if top == -1:
                result = 0
                break
            D = pop()
            if D == '{':
                if i != '}':
                    result = 0
                    break
            if D == '(':
                if i != ')':
                    result = 0
                    break
    if top != -1:
        result = 0
    print(f'#{t}', result)