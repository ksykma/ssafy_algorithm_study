# SW Expert Academy 0213_Stack1 - 1234

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
    
for t in range(1, 11):
    N, lst = input().split()
    N =  int(N)
    S = [0] * N
    top = -1
    push(lst[0])
    for i in range(1, N):
        push(lst[i])
        if lst[i] == S[top-1]:
            pop()
            pop()
    print(f'#{t}')
    for i in range(top+1):
        print(S[i], end='')
    print()