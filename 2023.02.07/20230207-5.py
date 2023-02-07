# SW Expert Academy 0207_List02 - 12392

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_val = 0
    min_val = 100
    result = []
    count = 0
    while count < 5:
        for i in lst:
            if i > max_val:
                max_val = i
            if i < min_val:
                min_val = i
        result.append(max_val)
        result.append(min_val)
        lst.remove(max_val)
        lst.remove(min_val)
        max_val = 0
        min_val = 100
        count += 1
    print(f'#{t}', *result)

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     for i in range(N-1):
#         idx = i    

#         if i%2 == 0:
#             for j in range(i+1, N):            
#                 if arr[idx]<arr[j]:
#                     idx = j
#             arr[i], arr[idx] = arr[idx], arr[i]

#         else:
#             for j in range(i+1, N):            
#                 if arr[idx]>arr[j]:
#                     idx = j
#             arr[i], arr[idx] = arr[idx], arr[i]

#     lst = []
#     for i in range(10):
#         lst.append(arr[i])

#     print(f'#{tc}', *lst) 


# 신동민

# T = int(input())

# # 가장 큰 수, 가장 작은 수, 홀수는 내림차순, 짝수는 오름차순
# # 2개씩 늘려야지.

# for tc in range(1, T+1):
#     N = int(input())
#     arr = [*map(int, input().split())]

#     # 큰건 뒤에서 가고, 작은건 앞에서 가고.

#     for i in range(0, N-1, 2):
#         maxIdx = i
#         minIdx = i+1
#         for j in range(i+1, N):
#             if arr[maxIdx] < arr[j]:
#                 maxIdx = j
#         arr[maxIdx], arr[i] = arr[i], arr[maxIdx]
#         for j in range(i+2, N):
#             if arr[minIdx] > arr[j]:
#                 minIdx = j        
#         arr[minIdx], arr[i+1] = arr[i+1], arr[minIdx]

#     print(f'#{tc}', end=' ')
#     for i in range(10):
#         print(arr[i], end=' ')
#     print()


# 선다영

# T = int(input())    # 테스트케이스 개수 입력

# for tc in range(1, T + 1):    # 테스트케이스 개수 만큼 반복
#     N = int(input())    # 정수의 개수 입력
#     arr = list(map(int, input().split()))    # 정수의 배열

#     for i in range(N - 1):    # 0 ~ N - 1
#         minIdx = i
#         maxIdx = i
#         for j in range(i + 1, N):
#             if arr[j] < arr[minIdx]:
#                 minIdx = j
#             if arr[j] > arr[maxIdx]:
#                 maxIdx = j

#         if i % 2 == 0:
#             arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
#         else:
#             arr[i], arr[minIdx] = arr[minIdx], arr[i]

#     print(f'#{tc}', end=' ')
#     for r in range(10):
#         print(arr[r], end=' ')
#     print()