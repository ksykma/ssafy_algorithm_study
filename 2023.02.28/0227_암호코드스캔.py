# SW Expert Academy 0227_Start - 1242

import sys
sys.stdin = open('input.txt', 'r')

dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
dict_2 = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
          '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
          '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
          'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}
# T = int(input())
# for t in range(1, T + 1):
N, M = list(map(int, input().split()))
lst = []
for i in range(N):
    secret = input()
    for j in secret:
        if j != '0':
            a = secret.rstrip('0')
            if a not in lst:
                lst.append(a)
# print(format(int('D26DDDAF76F5E8', 16), 'b'))
lst2 = []
for i in range(len(lst)):
    num = ''
    for j in range(len(lst[i])):
        num += dict_2[lst[i][j]]
    lst2.append(num.rstrip('0'))
lst3 = []

for i in range(len(lst2)):
    plus = 0
    length = len(lst2[i])-1
    print(len(lst2[i]))
    print(length)
    while length:
        if lst2[i][length] != lst2[i][length-1]:
            plus += 1
            if plus == 32:
                lst3.append(lst2[i][length:])
                # print(lst2[i][length:])
                lst2[i] = lst2[i][:length]
                plus = 0
        length -= 1
print(lst3)

    #     for j in range(len(lst2[i])-1, 0, -1):
    #         if lst2[i][j] != lst2[i][j-1]:
    #             plus += 1
    #             if plus == 32:
    #                 lst3.append(lst2[i][plus:])
                    
    #                 plus = 0
    # print(lst2)
        
                # for k in b:
                #     num_16 = bin(int(k.strip('0'), 16))[2:].rstrip('0')
                #     if num_16 not in lst:
                #         lst.append(num_16)
    # n = 1
    # for i in range(len(lst)):
    #     while True:
    #         if len(lst[i]) > 56*n:
    #             n += 1
    #         else:
    #             lst[i] = lst[i].zfill(56*n)
    #             n = 1
    #             break
    # num = []
    # for i in range(len(lst)):
    #     result = ''
    #     mok = len(lst[i]) // 56
    #     for j in range(0, len(lst[i]), mok):
    #         result += lst[i][j]
    #     num.append(result)
    # left = []
    # right = []
    # for i in range(0, len(num), 7):
    #     jjin = dict[num[i:i+7]]
    #     if (i+1) % 2 == 1:
    #         left.append(jjin)
    #     else:
    #         right.append(jjin)
    # print(left)
    # print(right)
    
                # a = bin(int(secret, 16))[2:]
        #         if a not in num:
        #             num.append(a)

        # print(num)
# lst = []
# for i in range(len(num)):
#     word = '0'
#     plus = 1
#     for j in range(1, len(num[i])):
#         if word[-1] != num[i][j]:
#             word += num[i][j]
#             plus += 1
#             if plus == 32:
#                 lst.append(word)
#                 word = '0'
#                 plus = 0
#         else:
#             word += num[i][j]
# print(lst)


