# SW Expert Academy 0227_Start - 1242

import sys
sys.stdin = open('input.txt', 'r')

dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
dict_2 = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
          '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
          '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
          'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = []
    # 0이아닌 다른것이 들어있으면 오른쪽 0들을 지우고 해당 값을 이진수로 변경하여 리스트에 추가
    for i in range(N):
        secret = input()
        for j in secret:
            if j != '0':
                a = secret.strip().rstrip('0')
                num = ''
                for k in range(len(a)):
                    num += dict_2[a[k]]
                num = num.strip().rstrip('0')
                if num not in lst:
                    lst.append(num)
    # print(lst)
    # lst2 = []
    # 
    # for i in range(len(lst)):
    #     num = ''
    #     for j in range(len(lst[i])):
    #         num += dict_2[lst[i][j]]
    #     lst2.append(num.rstrip('0'))
    # 오른쪽부터 확인하면서 원하는 값들을 추출
    lst3 = []
    for i in range(len(lst)):
        plus = 0
        length = len(lst[i])-1
        compare = lst[i]
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
    # 원하는 값을 56의 배수로 만들어주기
    n = 1
    for i in range(len(lst3)):
        while True:
            if len(lst3[i]) > 56*n:
                n += 1
            else:
                lst3[i] = lst3[i].zfill(56*n)
                n = 1
                break
    # 원하는 값을 56개의 문자열로 만들어주기
    lst4 = []
    for i in range(len(lst3)):
        result = ''
        mok = len(lst3[i]) // 56
        for j in range(0, len(lst3[i]), mok):
            result += lst3[i][j]
        lst4.append(result)
    lst4 = list(set(lst4))
    # 해당 문자열을 원하는 값으로 변경, 변경한 값들의 합이 10의 배수인지 확인, 맞으면 합해주기
    ans = 0
    ans_lst = []
    for i in range(len(lst4)):
        result_lst = []
        for j in range(0, len(lst4[i]), 7):
            result_lst.append(dict[lst4[i][j:j+7]])
        num_sum = 0
        for k in range(len(result_lst)):
            if (k+1) % 2 == 1:
                num_sum += result_lst[k] * 3
            else:
                num_sum += result_lst[k]
        if num_sum % 10 == 0:
            ans += sum(result_lst)
    print(f'#{t}', ans)
    
    
    
    
    
    
    
    
    # ans = 0
    # ans_lst = []
    # for i in range(len(lst4)):
    #     left = []
    #     right = []
    #     for j in range(0, len(lst4[i]), 7):
    #         jjin = dict[lst4[i][j:j+7]]
    #         if (j+1) % 2 == 1:
    #             left.append(jjin)
    #         else:
    #             right.append(jjin)
    #     if ((sum(left) * 3) + sum(right)) % 10 == 0:
    #         ans_lst.append(sum(left) + sum(right))
    # print(f'#{t}', sum(ans_lst))



