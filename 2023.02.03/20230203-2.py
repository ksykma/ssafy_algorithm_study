# SW Expert Academy 0202_List01 - 13616
# import sys
# sys.stdin = open('input.txt', 'r')

# T = int(input())

# for t in range(1, T + 1):
#     N = int(input())
#     a = b = c = d = e = 0
#     while True:
#         if N != 1:
#             if N % 2 == 0:
#                 N = N // 2
#                 a += 1
#             elif N % 3 == 0:
#                 N = N // 3
#                 b += 1
#             elif N % 5 == 0:
#                 N = N // 5
#                 c += 1
#             elif N % 7 == 0:
#                 N = N // 7
#                 d += 1
#             elif N % 11 == 0:
#                 N = N // 11
#                 e += 1
#         else:
#             break
#     print(f"#{t} {a} {b} {c} {d} {e}")

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    a = b = c = d = e = 0
    while True:
        if N != 1:
            if N % 2 == 0:
                N = N // 2
                a += 1
            elif N % 3 == 0:
                N = N // 3
                b += 1
            elif N % 5 == 0:
                N = N // 5
                c += 1
            elif N % 7 == 0:
                N = N // 7
                d += 1
            elif N % 11 == 0:
                N = N // 11
                e += 1
        else:
            break
    print(f"#{t} {a} {b} {c} {d} {e}")