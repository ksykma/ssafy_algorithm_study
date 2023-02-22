# SW Expert Academy 0217_문제풀이3 - 10760

import sys
sys.stdin = open('input.txt', 'r')
for t in range(1, 11):
    N, char = input().split()
    S = []
    for i in char:
        if len(S) == 0:
            S.append(i)
        elif S[-1] == i:
            S.pop()
        else:
            S.append(i)
    result = ''
    for i in S:
        result += i
    print(f'#{t}', result)