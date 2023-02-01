# SW Expert Academy 0201_List01 - 12387
import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
# for i in range(1, T + 1):
#     N, M = map(int,input().split())
#     lst = list(map(int,input().split()))
#     lst2 = []
#     for j in range(N - M + 1):
#         lst2.append(sum(lst[j:M+j]))
#     print(max(lst2) - min(lst2))

# T = int(input())
# for i in range(1, T + 1):
#     N, M = map(int,input().split())
#     lst = list(map(int,input().split()))
#     lst2 = []
#     for j in range(N - M + 1):
#         num = 0
#         for k in lst[j:M+j]:
#             num += k
#         lst2.append(num)
#     mini = lst2[0]
#     for min_val in lst2:
#         if min_val < mini:
#             mini = min_val
#     maxi = lst2[0]
#     for max_val in lst2 : 
#         if max_val > maxi:
#             maxi = max_val
#     print(f"#{i} {maxi - mini}")

# T = int(input())
# for i in range(1, T + 1):
#     N, M = map(int,input().split())
#     lst = list(map(int,input().split()))
#     min_val = 10000 * M
#     max_val = 0
#     for j in range(N - M + 1):
#         num = 0
#         for k in lst[j:M+j]:
#             num += k
#         if num > max_val:
#             max_val = num
#         if num < min_val:
#             min_val = num
#     print(f"#{i} {max_val - min_val}")

T = int(input())
for i in range(1, T + 1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    min_val = 10000 * M
    max_val = 0
    for j in range(N - M + 1):
        num = 0
        for k in range(M):
            num += lst[j+k]
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    print(f"#{i} {max_val - min_val}")
        