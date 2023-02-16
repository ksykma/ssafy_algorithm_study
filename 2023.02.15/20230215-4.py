# SW Expert Academy 0214_Stack1 - 1859   

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

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int,input().split()))
    S = [0] * N
    top = -1
    max_val = nums[-1]
    result = 0
    for i in range(N-1, 0, -1):
        cnt = 0
        if nums[i - 1] > max_val:
            if top == -1:
                max_val = nums[i - 1]
            else:
                top_cnt = top + 1
                while top != -1:
                    cnt += S[top]
                    pop()
                result += (max_val * top_cnt) - cnt
                max_val = nums[i - 1]

        else:
            push(nums[i - 1])
    top_cnt = top + 1
    while top != -1:
        cnt += S[top]
        pop()
    result += (max_val * top_cnt) - cnt
    print(f'#{t}', result)


# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int,input().split()))
#     S = [0] * N
#     top = -1
#     result = 0
#     max_val = 0
#     max_idx = 0
#     a = 0
#     while a < N:
#         cnt = 0
#         for i in range(a, N):
#             if max_val < nums[i]:
#                 max_val = nums[i]
#                 max_idx = i
#         for i in range(a, max_idx):
#             cnt += nums[i]
#         result += (max_val * (max_idx - a)) - cnt
#         a = max_idx + 1
#         max_val = 0
#     print(f'#{t}', result)

# for i in range(N-1):
#     cnt = 0
#     if nums[i] <= nums[i+1]:
#         push(nums[i])
#     else:
#         if top == -1:
#             push(nums[i])
#         else:
#             top_cnt = top + 1
#             while top != -1:
#                 cnt += S[top]
#                 pop()
#             result += (nums[i] * top_cnt) - cnt
# top_cnt = top + 1
# while top != -1:
#     cnt += S[top]
#     pop()
# result += (nums[-1] * top_cnt) - cnt
# print(result)