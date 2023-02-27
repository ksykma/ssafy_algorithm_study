# SW Expert Academy 0220_Queue - 11650    

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    T = int(input())
    lst = list(map(int, input().split()))
    result = 1
    while result:
        for i in range(1, 6):
            num = lst.pop(0)
            if num - i <= 0:
                lst.append(0)
                result = 0
                break
            else:
                lst.append(num - i)
    print(f'#{t}', *lst)
