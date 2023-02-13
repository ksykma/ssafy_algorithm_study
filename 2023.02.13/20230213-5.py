# SW Expert Academy 0213_Stack1 - 12399

import sys
sys.stdin = open('input.txt', 'r')

# def pop(idx):
#     global top
#     top -= 1
#     return words.pop(idx)

T = int(input())
for t in range(1, T + 1):
    words = list(input())
    N = len(words)
    top = N - 1
    i = 0
    while True:
        if i == len(words)-1:
            break
        else:
            if words[i] == words[i + 1]:
                words.pop(i)
                words.pop(i)
                if i == 0:
                    i -= 1
                else:
                    i -= 2
            i += 1
    result = 0
    for i in words:
        result += 1
    print(f'#{t}', result)