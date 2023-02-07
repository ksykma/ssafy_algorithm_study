# SW Expert Academy 0207_List02 - 1210

import sys
sys.stdin = open('input.txt', 'r')


for t in range(1, 11):
    n = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    for i in range(100):
        if arr[99][i] == 2:
            g = i
    h = 99
    while h >= 1:
        h -= 1
        if g == 0:
            if arr[h][g+1] == 1:
                while arr[h][g] >= 1:
                    g += 1
                g -= 1
        elif g == 99:
            if arr[h][g-1] == 1:
                while arr[h][g] >= 1:
                    g -= 1
                g += 1
        else:
            if arr[h][g-1] == 1:
                while arr[h][g] >= 1:
                    g -= 1
                g += 1
            elif arr[h][g+1] == 1:
                while arr[h][g] >= 1:
                    g += 1
                g -= 1

    print(f'#{t} {g-1}')
    

# for tc in range(1,11):
#     n = int(input())
    
#     # 입력값 각 행을 리스트로 하는 원소를 갖는 리스트 생성
#     arr = []
#     for i in range(100):
#         arr.append(list(map(int, input().split())))
        
#     # 맨 마지막 줄 2의 인덱스 (r=99, c=?)
#     for i in range(100):
#         if arr[99][i]==2:
#             c = i     

#     # 기준 r=99, c=i
#     r = 99
#     k = 0
#     while r >= 1:
#         if c >= 1 and arr[r][c-1] == 1 and k != 1:        # c-1>=0 이어야해서
#             c -= 1
#             k = -1
#         elif c <= 98 and arr[r][c+1] == 1 and k != -1:    # c+1<=99 이어야해서
#             c += 1
#             k = 1
#         elif arr[r-1][c] == 1:
#             r -= 1
#             k = 0
            
#     print(f'#{tc} {c}')  


# 신동민


# for _ in range(10):
#     T = int(input())
#     arr = [[0] + [*map(int, input().split())] + [0] for _ in range(100)]

#     min_cnt = 10000
#     for i in range(101):
#         if arr[0][i] != 1:
#             continue
        
#         row = 0
#         col = i
#         cnt = 0
#         # 기본적으로 row가 99면 멈춰야 함.
#         while row < 99:
#             if arr[row][col+1] == 1:
#                 while True:
#                     if arr[row][col+1] == 0:
#                         row += 1
#                         break
#                     else:
#                         col += 1
#             elif arr[row][col-1] == 1:
#                 while True:
#                     if arr[row][col-1] == 0:
#                         row += 1
#                         break
#                     else:
#                         col -= 1
#             else:
#                 row += 1
#         if arr[row][col] == 2:
#             print(f'#{T} {i-1}')
#             break


#                 #대각선이 1이면. 그쪽으로 가기.
#                 # while 0을 만날 때까지. 
#                 # 0을 만나면 아래로 가기.