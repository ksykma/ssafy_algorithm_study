# SW Expert Academy 0202_List01 - 12385

# 종점 N번 정류장
# 한번 충전으로 이동할 수 있는 정류장 수 K
# 충전기가 설치된 정류장 수 M
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는가?
# 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 0 출력
# 출발지에는 충전기 설치되어있지만 충전횟수에는 포함되지 않음
# import sys
# sys.stdin = open('input.txt', 'r')
# T = int(input())
# for t in range(1, T + 1):
#     K, N, M = list(map(int, input().split()))
#     # [0] + [1, 3, 5, 7, 9] + [N]
#     M_lst = [0] + list(map(int, input().split())) + [N]
#     # 1. 안되는 경우 인접한 두 충전소의 거리가 K보다 크면
#     cur = ans = 0
#     for i in range(1, M + 2):
#         if M_lst[i - 1] + K < M_lst[i]:
#             ans = 0
#             break
#         if cur + K < M_lst[i]:
#             cur = M_lst[i - 1]
#             ans += 1
#     print(f"#{t} {ans}")

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))
    cur = 0
    cnt = 0
    while cur + K < N:
        for a in range(cur + K, cur, -1):
            if a in M_lst:
                cur = a
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f"#{t} {cnt}")
    
        

