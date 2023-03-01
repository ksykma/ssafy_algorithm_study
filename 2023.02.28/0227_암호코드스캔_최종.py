# SW Expert Academy 0227_Start - 1242

import sys
sys.stdin = open('input.txt', 'r')

dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
dict_2 = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
          '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
          '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
          'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}
check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
  
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]
    lst = []
    for i in range(N):
        for j in check:
            if j in arr[i]:
                a = arr[i].strip().rstrip('0')
                if a not in lst:
                    lst.append(a)
    lst2 = []
    for i in range(len(lst)):
        num = ''
        for j in range(len(lst[i])):
            num += dict_2[lst[i][j]]
        lst2.append(num.strip().rstrip('0'))
  
    lst3 = []
    for i in range(len(lst2)):
        plus = 0
        length = len(lst2[i])-1
        compare = lst2[i]
        while compare:
            if compare[length] != compare[length-1]:
                plus += 1
                if plus == 31:
                    if compare[length:] not in lst3:
                        put = str(compare[length:])
                        lst3.append(put.strip().lstrip('0'))
                    compare = str(compare[:length])
                    compare = compare.strip().rstrip('0')
                    length = len(compare)-1
                    plus = 0
            length -= 1
  
    n = 1
    for i in range(len(lst3)):
        while True:
            if len(lst3[i]) > 56*n:
                n += 1
            else:
                lst3[i] = lst3[i].zfill(56*n)
                n = 1
                break
  
    lst4 = []
    for i in range(len(lst3)):
        result = ''
        mok = len(lst3[i]) // 56
        for j in range(0, len(lst3[i]), mok):
            result += lst3[i][j]
        lst4.append(result)
    lst4 = list(set(lst4))
  
    ans = 0
    ans_lst = []
    for i in range(len(lst4)):
        left = []
        right = []
        for j in range(0, len(lst4[i]), 7):
            jjin = dict[lst4[i][j:j+7]]
            if (j+1) % 2 == 1:
                left.append(jjin)
            else:
                right.append(jjin)
        if ((sum(left) * 3) + sum(right)) % 10 == 0:
            ans_lst.append(sum(left) + sum(right))
    print(f'#{t}', sum(ans_lst))