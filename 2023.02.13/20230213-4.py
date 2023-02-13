# SW Expert Academy 0213_Stack1 - 11573

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    S = [0] * 30
    top = -1
    for i in nums:
        if i != 0:
            top += 1
            S[top] = i
        else:
            top -= 1
    result = 0
    for i in range(top+1):
        result += S[i]
    print(f'#{t}', result)
# def push(item):
#     global top
#     top += 1
#     S[top] = item
#
# def pop():
#     global top
#     ret = S[top]
#     top -= 1
#     return ret
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     S = [0] * 30
#     top = -1
#     for i in nums:
#         if i != 0:
#             push(i)
#         else:
#             pop()
#     result = 0
#     for i in range(top + 1):
#         result += S[i]
#     print(f'#{t}', result)