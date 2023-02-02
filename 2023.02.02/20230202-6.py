# SW Expert Academy 0202_List01 - 12385

# 종점 N번 정류장
# 한번 충전으로 이동할 수 있는 정류장 수 K
# 충전기가 설치된 정류장 수 M
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는가?
# 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 0 출력
# 출발지에는 충전기 설치되어있지만 충전횟수에는 포함되지 않음

T = int(input())
for t in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))
    count = 0
    # for n in range(N):
    for m in M :
        if M_lst[m + 1] - M_lst[m] > K:
            print(f"#{t} 0")
        else:
            for mm in range(m + 2, M):
                if M_lst[m + mm] - M_lst[m] > K:
                    count += 1
