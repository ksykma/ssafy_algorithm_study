# SW Expert Academy 0227_Start - 1240

import sys
sys.stdin = open('input.txt', 'r')

dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    for i in range(N):
        nums = input()
        if '1' in nums:
            word = nums
            pass
    result = word.rstrip('0')
    result2 = result[len(result)-56:]

    left = []
    right = []
    n = 1
    ans = 0
    while result2:
        a = result2[:7]
        result2 = result2[7:]
        if n % 2 == 1:
            left.append(dict[a])
        else:
            right.append(dict[a])
        n += 1
    if ((sum(left) * 3) + sum(right)) % 10 == 0:
        ans = sum(left) + sum(right)
    print(f'#{t}', ans)


