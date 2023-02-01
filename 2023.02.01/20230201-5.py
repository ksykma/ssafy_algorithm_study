# SW Expert Academy 0201_List01 - 1206
import sys
sys.stdin = open('input.txt', 'r')

# 1번 풀이

for i in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    count = 0
    for j in range(N-4):
        max_lst = []
        group = []
        for k in range(5):
            group.append(lst[j+k])
        for g in range(5):
            if group[2] > group[0] and group[2] > group[1] and group[2] > group[3] and group[2] > group[4]:
                max_lst.append(group[g])
        if max_lst != []:
            for n in range(5):
                for s in range(4):
                    if max_lst[s] < max_lst[s + 1]:
                        max_lst[s], max_lst[s + 1] = max_lst[s + 1], max_lst[s]
            count += (max_lst[0] - max_lst[1])
 
    print(f"#{i} {count}")


# 2번 풀이

# for i in range(1, 11):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     count = 0
#     for j in range(2, N-2):
#         group = lst[j-2:j+3]
#         group.sort(reverse=True)
#         if lst[j] == group[0]:
#             count += (group[0] - group[1])
 
#     print(f"#{i} {count}")


