# SW Expert Academy 0206_List02 - 1209

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    num = int(input())
    result = 0
    lst = []
    for all_lst in range(100):
        nums = list(map(int, input().split()))
        lst.append(nums)
    for i in range(100):
        num_sum1 = 0
        num_sum2 = 0
        num_sum3 = 0
        num_sum4 = 0
        for j in range(100):
            num_sum1 += lst[i][j]
            num_sum2 += lst[j][i]
            if i == j:
                num_sum3 += lst[i][j]
                num_sum4 += lst[j][i]
        if num_sum1 > result:
            result = num_sum1
        if num_sum2 > result:
            result = num_sum2
        if num_sum3 > result:
            result = num_sum3
        if num_sum4 > result:
            result = num_sum4   
    print(f'#{t} {result}')
