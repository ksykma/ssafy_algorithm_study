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
K, N, M = list(map(int, input().split()))
M_lst = list(map(int, input().split()))
for m in range(M - 1) :
    if M_lst[m + 1] - M_lst[m] > K or N - M_lst[-1] > K:
        print(f"# 0")
    else:
        n = 0
        mm = 0
        count = 0
        while n <= N:
            while mm < M:
                if M_lst[mm] - n < K:
                    mm += 1
                    continue
                else:
                    count += 1
                    n = M_lst[mm]
            if mm == 5:
                if N - n >= K:
                    n += n
                    count += 1
                else:
                    n += N
print(f"# {count}")
