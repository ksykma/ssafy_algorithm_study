# SW Expert Academy 0215_Stack2 - 1222  

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    arr = input()
    S = []
    top = -1
    result = ''
    for i in range(N):
        if arr[i] == '+':
            if top == -1:
                top += 1
                S.append(arr[i])
            else:
                result += arr[i]
        else:
            result += arr[i]
    result += S[top]
    S.pop()
    top -= 1
    for i in range(N):
        if result[i] == '+':
            a = S.pop()
            b = S.pop()
            S.append(a + b)
        else:
            S.append(int(result[i]))
    print(f'#{t}', S[0])