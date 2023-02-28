# SW Expert Academy 0227_Start - 1240

import sys
sys.stdin = open('input.txt', 'r')

dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    nums = [input() for _ in range(N)]
    word = ''
    for i in range(N):
        if '1' in nums[i]:
            word = nums[i]
            break
    result = word.rstrip('0')
    result2 = result[len(result)-56:]

    lst = []
    ans = 0
    for i in range(0, 56, 7):
        lst.append(result2[i:i+7])
    num_sum = 0
    for i in range(8):
        if (i+1) % 2 == 1:
            num_sum += dict[lst[i]] * 3
        else:
            num_sum += dict[lst[i]]
    for i in range(8):
        if num_sum % 10 == 0:
            ans += dict[lst[i]]
    print(f'#{t}', ans)
    # left = []
    # right = []
    # n = 1
    # ans = 0
    # while result2:
    #     a = result2[:7]
    #     result2 = result2[7:]
    #     if n % 2 == 1:
    #         left.append(dict[a])
    #     else:
    #         right.append(dict[a])
    #     n += 1
    # if ((sum(left) * 3) + sum(right)) % 10 == 0:
    #     ans = sum(left) + sum(right)
    # print(f'#{t}', ans)


