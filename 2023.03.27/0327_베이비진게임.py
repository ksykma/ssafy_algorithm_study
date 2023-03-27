# 백준 2292 탐욕_베이비진 게임

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    player1 = []
    player2 = []
    result = 0
    for j in range(0, 12, 2):
        player1.append(nums[j])
        player2.append(nums[j+1])
        if len(player1)>=3:
            for i in range(len(player1)):
                cnt = 1
                if player1.count(player1[i]) == 3:
                    result = 1
                    break
                if player1[i]-1 in player1:
                    cnt += 1
                if player1[i]+1 in player1:
                    cnt += 1
                if cnt == 3:
                    result = 1
                    break
            if result == 0:
                for k in range(len(player2)):
                    cnt = 1
                    if player2.count(player2[k]) == 3:
                        result = 2
                        break
                    if player2[k]-1 in player2:
                        cnt += 1
                    if player2[k]+1 in player2:
                        cnt += 1
                    if cnt == 3:
                        result = 2
                        break
        if result != 0:
            break
                
    print(f'#{t}', result)