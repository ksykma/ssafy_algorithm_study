# SW Expert Academy 0208_String - 12395

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_val = 0
    cnt = 0
    for i in str1:
        for j in str2:
            if i == j:
                cnt += 1
        if max_val < cnt:
            max_val = cnt
        cnt = 0
    print(f'#{t} {max_val}')

# 교수님 풀이
    # T = int(input())
    # for t in range(1, T + 1):
    #     str1 = input()
    #     str2 = input()

    #     # 메모리를 추가적으로 사용해서 쉽게 작성
    #     cnt = [0] * 128 # ASCII 코드값을 배열의 인덱스로 사용

    #     for ch2 in str2:
    #         cnt[ord(ch2)] += 1

    #     ans = 0
    #     for ch1 in str1:
    #         if ans < cnt[ord(ch1)]:
    #             ans = cnt[ord(ch1)]
    #     print(ans)