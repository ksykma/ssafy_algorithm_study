# SW Expert Academy 0220_Queue - 11650    

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    result = 1
    while result:
        for i in range(1, 6):
            num = arr.pop(0)
            num -= i
            if num <= 0:
                result = 0
                arr.append(0)
                break
            arr.append(num)
    print(f'#{t}', *arr)