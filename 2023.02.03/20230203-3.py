# SW Expert Academy 0202_List01 - 9386

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = input()
    max_val = 0
    result = 0
    for i in str(nums):
        if int(i) == 1:
            result += 1
        else:
            result = 0
        if max_val < result:
                max_val = result
    print(f"#{t} {max_val}")
    
