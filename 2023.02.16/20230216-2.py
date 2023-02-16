# SW Expert Academy 0215_Stack2 - 11613   

import sys
sys.stdin = open('input.txt', 'r')

forchick = ['+', '-', '*', '/']
T = int(input())
for t in range(1, T + 1):
    nums = input().split()
    N = len(nums)
    S = [] * N
    for i in range(N):
        if nums[i] in forchick:
            if len(S) < 2:
                print(f'#{t} error')
                break
            else:
                b = S.pop()
                a = S.pop()
                if nums[i] == '+':
                    S.append(a + b)
                elif nums[i] == '-':
                    S.append(a - b)
                elif nums[i] == '*':
                    S.append(a * b)
                else:
                    S.append(a // b)
        elif nums[i] == '.':
            if len(S) >= 2:
                print(f'#{t} error')
            else:
                print(f'#{t}', S[0])
        else:
            S.append(int(nums[i]))