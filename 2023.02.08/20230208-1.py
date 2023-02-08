# SW Expert Academy 0208_String - 12393

import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
# for t in range(1, T + 1):
#     str1 = input()
#     str2 = input()
#     if str1 in str2:
#         print(f'#{t} 1')
#     else:
#         print(f'#{t} 0')


T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    ans = 0
    for i in range(M - N + 1):
        for j in range(N):
            if str1[j] != str2[i+j]:
                break
        else:
            ans = 1

    print(f'#{tc} {ans}')
