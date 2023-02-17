# SW Expert Academy 0216_Stack2 - 1223

import sys
sys.stdin = open('input.txt', 'r')

def push(item):
    global top
    top += 1
    S[top] = item

def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

cal = {'*': 2, '+': 1}
for t in range(1, 11):
    N = int(input())
    lst = input()
    S = [0] * N
    top = -1
    char = ''
    for i in lst:
        if i in cal:
            if top == -1:
                push(i)
            elif cal[S[top]] > cal[i]:
                while top != -1:
                    char += S[top]
                    pop()
                push(i)
            elif cal[S[top]] == cal[i]:
                char += i
            else:
                push(i)
        else:
            char += i
    while top != -1:
        char += S[top]
        pop()
    for i in char:
        if i in ['+', '*']:
            b = S[top]
            pop()
            a = S[top]
            pop()
            if i == '+':
                result = a + b
                push(result)
            elif i == '*':
                result = a * b
                push(result)
        else:
            push(int(i))
    print(f'#{t} {S[0]}')




