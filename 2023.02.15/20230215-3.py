# SW Expert Academy 0214_Stack1 - 5432    

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
    LI = input()
    N = len(LI)
    S = [0] * N
    top = -1
    cnt = 0
    push(LI[0])
    for i in range(1, N):
        push(LI[i])
        if LI[i-1] == '(' and LI[i] == ')':
            pop()
            pop()
            cnt += top + 1
        else:
            if LI[i] == '(':
                pass
            elif LI[i] == ')':
                cnt += 1
                pop()
                pop()
    print(f'#{t}', cnt)
