# SW Expert Academy 0213_Stack1 - 12399

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
    words = list(input())
    N = len(words)
    S = [0] * N
    top = - 1
    push(words[0])
    for i in range(1, N):
        push(words[i])
        if words[i] == S[top-1]:
            pop()
            pop()
    print(f'#{t}', top+1)
        
    

# T = int(input())
# for t in range(1, T + 1):
#     words = list(input())
#     N = len(words)
#     i = 0
#     while True:
#         if i == len(words)-1:
#             break
#         else:
#             if words[i] == words[i + 1]:
#                 words.pop(i)
#                 words.pop(i)
#                 if i == 0:
#                     i -= 1
#                 else:
#                     i -= 2
#             i += 1
#     result = 0
#     for i in words:
#         result += 1
#     print(f'#{t}', result)