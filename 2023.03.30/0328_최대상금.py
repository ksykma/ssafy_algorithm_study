# SW Expert Academy 0328_완탐_탐욕 - 1244 최대 상금

import sys
sys.stdin = open('input.txt', 'r')

def money():
    ret = 0
    for val in nums:
        ret = ret*10 + val
    return ret


def find_max(k):
    global ans
    val = money()
    if val in visit[k]:
        return
    visit[k].add(val)

    if k == c:
        if ans < val:
            ans = val
    else:
        for i in range(N - 1):
            for j in range(i + 1, N):
                nums[i], nums[j] = nums[j], nums[i]
                find_max(k + 1)
                nums[i], nums[j] = nums[j], nums[i]
    

T = int(input())
for t in range(1, T + 1):
    nums, c = map(int, input().split())
    nums = list(map(int, list(str(nums))))
    ans = 0
    N = len(nums)
    visit = [set() for _ in range(c + 1)]
    print(visit)
    find_max(0)
    print(f'#{t}', ans)